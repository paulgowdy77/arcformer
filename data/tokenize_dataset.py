from arc_tokenizer import ArcTokenizer
import pickle
import numpy as np
import glob
import os

date_str = "train_set_1"
vocab_merge_path = 'data/vocab_merges_v1/train_set_1_processed_examples_bpe_MERGES.pkl'

tokenizer = ArcTokenizer(vocab_merge_path)

example_files = glob.glob(f'data/datasets_v1/{date_str}/processed_examples/*.pkl')
print("example files:", len(example_files))

# make encoded folder
if not os.path.exists(f'data/datasets_v1/{date_str}/encoded_files'):
    os.makedirs(f'data/datasets_v1/{date_str}/encoded_files')

for i, example_filename in enumerate(example_files):
    print('loading dataset slice', i)
    with open(example_filename, 'rb') as f:
        test_dataset = pickle.load(f)
    # flatten
    test_dataset = [item for sublist in test_dataset for item in sublist]
    print('tokenizing dataset slice', i)
    encoded_test = tokenizer.encode(test_dataset)

    # save the encoded test dataset
    z = np.array(encoded_test, dtype=np.int16)
    print('saving dataset slice', i)
    np.save(f'data/datasets_v1/{date_str}/encoded_files/encoded_data_slice_{str(i)}.npy', z)
