import sys
sys.path.insert(1, 'C:/Users/paul/Documents/arcformer')

import os
import torch
import wandb
import time
from datetime import datetime
import math
from contextlib import nullcontext

from torch.utils.data import DataLoader
from ArcDatasetV1 import ArcDatasetV1
from training.model import GPTConfig, GPT

# wandb logging
wandb_log = True
wandb_project = 'arcformer'
date_time = datetime.now().strftime("%m_%d_%Y_%H:%M:%S")
wandb_run_name = 'arcformer_dev_'  + date_time

gradient_accumulation_steps = 5 * 8 # used to simulate larger batch sizes
batch_size = 2 # if gradient_accumulation_steps > 1, this is the micro-batch size
block_size = 2048
# model
n_layer = 16
n_head = 16
n_embd = 512
bias = False
dropout = 0.0

# adamw optimizer
learning_rate = 6e-4 # max learning rate
max_iters = 5000 # total number of training iterations
weight_decay = 1e-1
beta1 = 0.9
beta2 = 0.95
grad_clip = 1.0 # clip gradients at this value, or disable if == 0.0
# learning rate decay settings
decay_lr = True # whether to decay the learning rate
warmup_iters = 200 # how many steps to warm up for
lr_decay_iters = 600000 # should be ~= max_iters per Chinchilla
min_lr = 6e-5

device = 'cuda' if torch.cuda.is_available() else 'cpu'
dtype = 'bfloat16' if torch.cuda.is_available() and torch.cuda.is_bf16_supported() else 'float16' # 'float32', 'bfloat16', or 'float16', the latter will auto implement a GradScaler

iter_num = 0
best_val_loss = 1e9
master_process = True
eval_interval = 4
log_interval = 1
out_dir = 'out'

os.makedirs(out_dir, exist_ok=True)

print("-------")
print("device:", device)
print("dtype:", dtype)
print("-------")

device_type = 'cuda' if 'cuda' in device else 'cpu' # for later use in torch.autocast
ptdtype = {'float32': torch.float32, 'bfloat16': torch.bfloat16, 'float16': torch.float16}[dtype]
ctx = nullcontext() if device_type == 'cpu' else torch.amp.autocast(device_type=device_type, dtype=ptdtype)

# data
train_dataset = ArcDatasetV1(encoded_example_dir="data/datasets_v1/20240308-0920/encoded_files")
train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

val_dataset = ArcDatasetV1(encoded_example_dir="data/datasets_v1/20240309-1309/encoded_files")
val_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

DATALOADER_SPLITS = {
    'train': train_dataloader,
    'val': val_dataloader,
    'test': None
}


config_keys = [k for k,v in globals().items() if not k.startswith('_') and isinstance(v, (int, float, bool, str))]
#exec(open('configurator.py').read()) # overrides from command line or config file
config = {k: globals()[k] for k in config_keys} # will be useful for logging


model_args = dict(
    n_layer=n_layer, 
    n_head=n_head, 
    n_embd=n_embd, 
    block_size=block_size,
    bias=bias, 
    vocab_size=None,
    dropout=dropout
    )


print("Initializing a new model from scratch")
# determine the vocab size we'll use for from-scratch training
model_args['vocab_size'] = 256
gptconf = GPTConfig(**model_args)
model = GPT(gptconf)
model.to(device)

# initialize a GradScaler. If enabled=False scaler is a no-op
scaler = torch.cuda.amp.GradScaler(enabled=(dtype == 'float16'))

# optimizer
optimizer = model.configure_optimizers(weight_decay, learning_rate, (beta1, beta2), device_type)
checkpoint = None # free up memory

# helps estimate an arbitrarily accurate loss over either split using many batches
@torch.no_grad()
def estimate_loss():
    out = {}
    model.eval()
    #for split in ['train']:
    for split, loader in DATALOADER_SPLITS.items():
        if loader is None:
            continue
        losses = torch.zeros(10)
        for k in range(10):
            X, Y = get_batch(loader)
            with ctx:
                logits, loss = model(X, Y)
            losses[k] = loss.item()
        out[split] = losses.mean()
    model.train()
    return out

# def estimate_loss():
#     out = {}
#     model.eval()
#     for split in ['train']:
#         losses = torch.zeros(10)
#         for k in range(10):
#             X, Y = get_batch()
#             with ctx:
#                 logits, loss = model(X, Y)
#             losses[k] = loss.item()
#         out[split] = losses.mean()
#     model.train()
#     return out

# learning rate decay scheduler (cosine with warmup)
def get_lr(it):
    # 1) linear warmup for warmup_iters steps
    if it < warmup_iters:
        return learning_rate * it / warmup_iters
    # 2) if it > lr_decay_iters, return min learning rate
    if it > lr_decay_iters:
        return min_lr
    # 3) in between, use cosine decay down to min learning rate
    decay_ratio = (it - warmup_iters) / (lr_decay_iters - warmup_iters)
    assert 0 <= decay_ratio <= 1
    coeff = 0.5 * (1.0 + math.cos(math.pi * decay_ratio)) # coeff ranges 0..1
    return min_lr + coeff * (learning_rate - min_lr)


    
wandb.init(project=wandb_project, name=wandb_run_name, config=config)

def get_batch(dataloader):
    x, y = next(iter(dataloader))
    if device_type == 'cuda':
        # pin arrays x,y, which allows us to move them to GPU asynchronously (non_blocking=True)
        x, y = x.pin_memory().to(device, non_blocking=True), y.pin_memory().to(device, non_blocking=True)
    else:
        x, y = x.to(device), y.to(device)
    return x, y

# training loop
X, Y = get_batch(train_dataloader)
t0 = time.time()
local_iter_num = 0 # number of iterations in the lifetime of this process
raw_model = model # unwrap DDP container if needed
running_mfu = -1.0






while True:

    # determine and set the learning rate for this iteration
    lr = get_lr(iter_num) if decay_lr else learning_rate
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr

    # evaluate the loss on train/val sets and write checkpoints
    if iter_num % eval_interval == 0 and master_process:
        losses = estimate_loss()
        #print(f"step {iter_num}: train loss {losses['train']:.4f}") #, val loss {losses['val']:.4f}")
        
        log_obj = {
                "iter": iter_num,
                "lr": lr,
                "mfu": running_mfu*100,
        }

        print("eval iter:", iter_num)
        for k, v in losses.items():
            print(f"{k} loss: {v:.4f}")
            log_obj[f"{k}_loss"] = v

        if wandb_log:
            wandb.log(log_obj)
        # if True: # losses['val'] < best_val_loss:# or always_save_checkpoint:
        #     #best_val_loss = losses['val']
        #     if iter_num > 0:
        #         checkpoint = {
        #             'model': raw_model.state_dict(),
        #             'optimizer': optimizer.state_dict(),
        #             'model_args': model_args,
        #             'iter_num': iter_num,
        #             #'best_val_loss': best_val_loss,
        #             'config': config,
        #         }
        #         print(f"saving checkpoint to {out_dir}")
        #         torch.save(checkpoint, os.path.join(out_dir, 'ckpt.pt'))

    # forward backward update, with optional gradient accumulation to simulate larger batch size
    # and using the GradScaler if data type is float16
    for micro_step in range(gradient_accumulation_steps):
        # if ddp:
        #     # in DDP training we only need to sync gradients at the last micro step.
        #     # the official way to do this is with model.no_sync() context manager, but
        #     # I really dislike that this bloats the code and forces us to repeat code
        #     # looking at the source of that context manager, it just toggles this variable
        #     model.require_backward_grad_sync = (micro_step == gradient_accumulation_steps - 1)
        with ctx:
            logits, loss = model(X, Y)
            loss = loss / gradient_accumulation_steps # scale the loss to account for gradient accumulation
        # immediately async prefetch next batch while model is doing the forward pass on the GPU
        X, Y = get_batch(train_dataloader)
        # backward pass, with gradient scaling if training in fp16
        scaler.scale(loss).backward()
    # clip the gradient
    if grad_clip != 0.0:
        scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), grad_clip)
    # step the optimizer and scaler if training in fp16
    scaler.step(optimizer)
    scaler.update()
    # flush the gradients as soon as we can, no need for this memory anymore
    optimizer.zero_grad(set_to_none=True)

    # timing and logging
    t1 = time.time()
    dt = t1 - t0
    t0 = t1

    if iter_num % log_interval == 0 and master_process:
        # get loss as float. note: this is a CPU-GPU sync point
        # scale up to undo the division above, approximating the true total loss (exact would have been a sum)
        lossf = loss.item() * gradient_accumulation_steps
        if local_iter_num >= 5: # let the training loop settle a bit
            mfu = raw_model.estimate_mfu(batch_size * gradient_accumulation_steps, dt)
            running_mfu = mfu if running_mfu == -1.0 else 0.9*running_mfu + 0.1*mfu
        print(f"iter {iter_num}: loss {lossf:.4f}, time {dt*1000:.2f}ms, mfu {running_mfu*100:.2f}%")
    iter_num += 1
    local_iter_num += 1

    # termination conditions
    if iter_num > max_iters:
        break