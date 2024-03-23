import pickle
import glob 
from plotter_utils import display_example_list


dataset_name = 'train_set_1'

pickled_examples = glob.glob(f'data/datasets_v1/{dataset_name}/pickled_examples/*.pkl')
print("pickled example files:", len(pickled_examples))

for i in range(3):
    with open(pickled_examples[i], 'rb') as f:
        example_sets = pickle.load(f)
    example_set = example_sets[0]\
    #display_example_list(example_set)


    # unpack here
    