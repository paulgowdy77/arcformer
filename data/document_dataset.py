import pickle
import glob 
from plotter_utils import display_example_list
from process_data_v1 import unpack_example_set
import os



dataset_name = 'train_set_1'
split_size = 50000

pickled_examples = glob.glob(f'data/datasets_v1/{dataset_name}/pickled_examples/*.pkl')
print("pickled example files:", len(pickled_examples))

# create processed documents folder
if not os.path.exists(f'data/datasets_v1/{dataset_name}/processed_documents'):
    os.makedirs(f'data/datasets_v1/{dataset_name}/processed_documents')

COLLECT_DOCUMENTS = []

for i in range(len(pickled_examples)):
    with open(pickled_examples[i], 'rb') as f:
        example_sets = pickle.load(f)

    for j in range(len(example_sets)):
        example_set = example_sets[j]
        #display_example_list(example_set)


        # unpack here
        unpacked_set = unpack_example_set(example_set, include_end_example_set=False)
        #print(len(unpacked_set))
        #print(unpacked_set[:20], unpacked_set[-20:])

        COLLECT_DOCUMENTS.append(unpacked_set)

print("total number of documents:", len(COLLECT_DOCUMENTS))

# split the documents into smaller chunks and save them
for i in range(0, len(COLLECT_DOCUMENTS), split_size):
    with open(f'data/datasets_v1/{dataset_name}/processed_documents/processed_documents_{i}.pkl', 'wb') as f:
        pickle.dump(COLLECT_DOCUMENTS[i:i+split_size], f)

        