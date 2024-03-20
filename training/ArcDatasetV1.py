import torch 
from torch.utils.data import Dataset
import glob 
import numpy as np 


class ARCDataLoader:

    def __init__(self, dataset, batch_size, shuffle=True):
        self.dataset = dataset
        self.batch_size = batch_size
        self.shuffle = shuffle

    def get_batch(self):
        batch_x = []
        batch_y = []
        for _ in range(self.batch_size):
            x, y = self.dataset[np.random.randint(0, len(self.dataset))]
            batch_x.append(x)
            batch_y.append(y)
        return np.array(batch_x), np.array(batch_y)


class ArcDatasetV1:

    def __init__(self, encoded_example_dir, block_size=2048, device='cpu', device_type='cpu'):
        self.encoded_example_dir = encoded_example_dir
        self.encoded_example_files = glob.glob(encoded_example_dir + "/*.npy")
        self.block_size = block_size

        # self.device = device
        # self.device_type = device_type

        self.data = []
        print("Loading data slices...")
        for file in self.encoded_example_files:
            loaded_array = np.load(file)
            self.data.append(loaded_array)

        self.data = np.concatenate(self.data, axis=0)

        print("Data shape:")
        print(self.data.shape)

    def __len__(self):
        return len(self.data)-self.block_size
    
    def __getitem__(self, idx):
        #x = torch.from_numpy((self.data[idx:idx+self.block_size]).astype(np.int64))
        #y = torch.from_numpy((self.data[idx+1:idx+1+self.block_size]).astype(np.int64))

        x = self.data[idx:idx+self.block_size].astype(np.int64)
        y = self.data[idx+1:idx+1+self.block_size].astype(np.int64)

        # if self.device_type == 'cuda':
        #     # pin arrays x,y, which allows us to move them to GPU asynchronously (non_blocking=True)
        #     x, y = x.pin_memory().to(self.device, non_blocking=True), y.pin_memory().to(self.device, non_blocking=True)
        # else:
        #     x, y = x.to(self.device), y.to(self.device)

        return x, y