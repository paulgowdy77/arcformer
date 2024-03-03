import pickle 

merge_file = 'data/datasets_v1/20240301-2016/processed_examples/processed_examples_bpe_MERGES.pkl'

with open(merge_file, 'rb') as f:
    merges = pickle.load(f)

print(merges.keys())
print(merges['token_count'])


print(merges)


vocab = {idx: idx  for idx in range(merges['token_count'])}
for (p0, p1), idx in merges['merges'].items():
    vocab[idx] = vocab[p0] + vocab[p1]

print(vocab)