from arc_tokenizer import ArcTokenizer
import pickle
import numpy as np
import glob
import os

tokenizer = ArcTokenizer('data/datasets_v1/20240303-2251/processed_examples_bpe_MERGES.pkl')


example_files = glob.glob('data/datasets_v1/20240303-2251/processed_examples/*.pkl')
print("example files:", len(example_files))

# make encoded folder
if not os.path.exists('data/datasets_v1/20240303-2251/encoded_files'):
    os.makedirs('data/datasets_v1/20240303-2251/encoded_files')

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
    np.save(f'data/datasets_v1/20240303-2251/encoded_files/encoded_data_slice_{str(i)}.npy', z)
