from arc_tokenizer import ArcTokenizer
import pickle
import numpy as np

tokenizer = ArcTokenizer('data/datasets_v1/20240303-2251/processed_examples_bpe_MERGES.pkl')

test_dataset_fn = 'data/datasets_v1/20240301-2016/processed_examples/processed_examples.pkl'
with open(test_dataset_fn, 'rb') as f:
    test_dataset = pickle.load(f)
# flatten
test_dataset = [item for sublist in test_dataset for item in sublist]

encoded_test = tokenizer.encode(test_dataset)

# save the encoded test dataset
z = np.array(encoded_test, dtype=np.int16)
print('saving dataset')
np.save('data/datasets_v1/20240301-2016/processed_examples/encoded_dataset_v1.npy', z)
