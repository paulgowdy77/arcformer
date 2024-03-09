import sys
sys.path.insert(1, 'C:/Users/paul/Documents/arcformer')

from torch.utils.data import DataLoader
from ArcDatasetV1 import ArcDatasetV1
from data.arc_tokenizer import ArcTokenizer
from data.plotter_utils import display_example_list



#tokenizer = ArcTokenizer('data/datasets_v1/20240308-0920/processed_examples_bpe_MERGES.pkl')

datasetv1 = ArcDatasetV1(encoded_example_dir="data/datasets_v1/20240308-0920/encoded_files")
train_dataloader = DataLoader(datasetv1, batch_size=16, shuffle=True)

# stub = datasetv1.data[:55000]
# decoded = tokenizer.decode(stub)
# # print(len(decoded))

x_batch, y_batch = next(iter(train_dataloader))
print(x_batch.shape)
print(y_batch.shape)

print(x_batch[3,:10])
print(y_batch[3,:10])


# def split_list(llist, split_token):
#     new_list = []
#     sub_list = []
#     for token in llist:
#         if token != split_token:
#             sub_list.append(token)
#         else:
#             new_list.append(sub_list)
#             sub_list = []

#     return new_list

# def deprocess_example_set(processed_example_set):
#     examples = split_list(processed_example_set, 13)
#     grids = [split_list(example, 12) for example in examples]

#     # split grids into rows
#     full_split = [
#             {
#                 "input": split_list(grid[0], 11),
#                 "output": split_list(grid[1], 11)
#             } 
#         for grid in grids
#     ]

#     return full_split

# example_sets = split_list(decoded, 14)
# print("example sets:", len(example_sets))

# for ex in example_sets:
#     print(len(ex))

# for k in range(10,12):
#     z = deprocess_example_set(example_sets[k])
#     display_example_list(z)