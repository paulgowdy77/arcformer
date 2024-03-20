import sys
sys.path.insert(1, '/home/paul/Documents/arcformer')

#from torch.utils.data import DataLoader
from ArcDatasetV1 import ArcDatasetV1, ARCDataLoader
from data.arc_tokenizer import ArcTokenizer
from data.plotter_utils import display_example_list



tokenizer = ArcTokenizer('data/datasets_v1/20240309-1950/processed_examples_bpe_MERGES.pkl')

block_size = 1024

train_dataset = ArcDatasetV1(
    encoded_example_dir="data/datasets_v1/20240309-1950/encoded_files", 
    block_size=block_size)
train_dataloader = ARCDataLoader(train_dataset, batch_size=2, shuffle=True)



for sample in range(10):
    x_batch, y_batch = train_dataloader.get_batch()


    x = x_batch[0]
    #print(x.shape)

    decoded_x = tokenizer.decode(x)

    #print(len(decoded_x))

    unique_tokens = set(decoded_x) 

    counts = {}
    for token in unique_tokens:
        counts[token] = decoded_x.count(token)

    # for token, count in counts.items():
    #     print(token, count)
    print(counts[14])


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