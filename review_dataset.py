import numpy as np
from data.arc_tokenizer import ArcTokenizer
from data.plotter_utils import display_example_list

dataset = 'data/datasets_v1/20240303-2251/encoded_files/encoded_data_slice_1.npy'

# load the encoded dataset
encoded_dataset = np.load(dataset)

print('encoded dataset:', encoded_dataset.shape)

stub = encoded_dataset[:]

#print('stub:', stub)

tokenizer = ArcTokenizer('data/datasets_v1/20240303-2251/processed_examples_bpe_MERGES.pkl')

decoded = tokenizer.decode(stub)

#print('decoded:', decoded)
print('decoded shape:', len(decoded))

print(sum([1 for token in decoded if token == 14]))

def split_list(llist, split_token):
    new_list = []
    sub_list = []
    for token in llist:
        if token != split_token:
            sub_list.append(token)
        else:
            new_list.append(sub_list)
            sub_list = []

    return new_list

def deprocess_example_set(processed_example_set):
    examples = split_list(processed_example_set, 13)
    grids = [split_list(example, 12) for example in examples]

    # split grids into rows
    full_split = [
            {
                "input": split_list(grid[0], 11),
                "output": split_list(grid[1], 11)
            } 
        for grid in grids
    ]

    return full_split

example_sets = split_list(decoded, 14)
print("example sets:", len(example_sets))

for k in range(40,45):
    z = deprocess_example_set(example_sets[k])
    display_example_list(z)