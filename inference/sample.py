import sys
sys.path.insert(1, '/home/paul/Documents/arcformer')

import torch
import os 
from training.model import GPTConfig, GPT
import numpy as np

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


# load test data

test_data_path = 'data/datasets_v1/val_set_1/encoded_files/encoded_data_slice_0.npy'
test_data = torch.from_numpy(np.load(test_data_path)).to(device)
print(test_data.shape)

def sample_data(data):
    i = np.random.randint(0, data.shape[0]-gptconf.block_size)
    x = data[i:i+gptconf.block_size]
    y = data[i+1:i+1+gptconf.block_size]
    yy = data[i:i+300+gptconf.block_size]
    return x, y, yy

x, y, yy = sample_data(test_data)

print(x[:230])
print(y[:203])

xx = x.unsqueeze(0)
# index dim needs to be int
xx = xx.long()

print(xx.shape)

prediction = model.generate(xx, 200, temperature=0.000001, top_k=1)

print(prediction.shape)
print(prediction)

for i in range(1400):
    print(i, prediction[0, i].item(), yy[i].item(), prediction[0, i].item() == yy[i].item())
    if i == 1023:
        print("================================")

# print(z.shape)

# z = z.to(device)
# model.eval()
# resp, loss = model(z)
# print(resp.shape)
# print(resp[0, 0, :])