import torch 
from torch.utils.data import Dataset
import glob 
import numpy as np 

class ArcDatasetV1:

    def __init__(self, encoded_example_dir, block_size=2048):
        self.encoded_example_dir = encoded_example_dir
        self.encoded_example_files = glob.glob(encoded_example_dir + "/*.npy")
        self.block_size = block_size

        self.data = []
        print("Loading data slices...")
        for file in self.encoded_example_files:
            loaded_array = np.load(file)
            self.data.append(loaded_array)

        self.data = np.concatenate(self.data, axis=0)

    def __len__(self):
        return len(self.data)-self.block_size
    
    def __getitem__(self, idx):
        x = torch.from_numpy((self.data[idx:idx+self.block_size]).astype(np.int64))
        y = torch.from_numpy((self.data[idx+1:idx+1+self.block_size]).astype(np.int64))
        return x, y