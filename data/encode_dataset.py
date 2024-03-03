import pickle 

merge_file = 'data/datasets_v1/20240301-2016/processed_examples/processed_examples_bpe_MERGES.pkl'

with open(merge_file, 'rb') as f:
    merges = pickle.load(f)

# print(merges.keys())
# print(merges['token_count'])
# print(merges['merges'])




vocab = {idx: idx for idx in range(merges['token_count'])}
for (p0, p1), idx in merges['merges'].items():
    # flattened list
    new = []
    if type(vocab[p0]) == int:
        new.append(vocab[p0])
    else:
        for e in vocab[p0]:
            new.append(e)
    if type(vocab[p1]) == int:
        new.append(vocab[p1])
    else:
        for e in vocab[p1]:
            new.append(e)
    vocab[idx] = new

#for k, v in vocab.items():
#    print(k, v)
    
def decode(tokens):
    decoded = []
    for token in tokens:
        if type(vocab[token]) == int:
            decoded.append(vocab[token])
        else:
            decoded.extend(vocab[token])
    return decoded

# test
print(decode([0, 1, 124, 3, 4, 5, 6, 7, 8, 9]))

