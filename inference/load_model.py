import sys
sys.path.insert(1, '/home/paul/Documents/arcformer')

import torch
import os 
from training.model import GPTConfig, GPT

#/home/paul/Documents/arcformer/training/out/good_one_long_run_REAL
out_dir = 'training/out/good_one_long_run_REAL'

device = 'cuda' if torch.cuda.is_available() else 'cpu'

print(f"Resuming training from {out_dir}")
    # resume training from a checkpoint.
ckpt_path = os.path.join(out_dir, 'ckpt.pt')
checkpoint = torch.load(ckpt_path, map_location=device)
checkpoint_model_args = checkpoint['model_args']
model_args = checkpoint_model_args

model_args['vocab_size'] = 256
gptconf = GPTConfig(**model_args)
model = GPT(gptconf)
model.to(device)


state_dict = checkpoint['model']
# fix the keys of the state dictionary :(
# honestly no idea how checkpoints sometimes get this prefix, have to debug more
unwanted_prefix = '_orig_mod.'
for k,v in list(state_dict.items()):
    if k.startswith(unwanted_prefix):
        state_dict[k[len(unwanted_prefix):]] = state_dict.pop(k)
model.load_state_dict(state_dict)
iter_num = checkpoint['iter_num']

print(iter_num)

z = torch.randint(0, 256, (2, 1024))

print(z.shape)

z = z.to(device)
model.eval()
resp, loss = model(z)
print(resp.shape)
print(resp[0, 0, :])