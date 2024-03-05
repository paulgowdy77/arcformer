import pickle 

merge_file = 'data/datasets_v1/20240301-2016/processed_examples/processed_examples_bpe_MERGES.pkl'

with open(merge_file, 'rb') as f:
    merges = pickle.load(f)

# print(merges.keys())
# print(merges['token_count'])
# print(merges['merges'])
    
def get_stats(ids):
    counts = {}
    for pair in zip(ids, ids[1:]):
        counts[pair] = counts.get(pair, 0) + 1
    return counts

def merge(ids, pair, idx):
  newids = []
  i = 0
  while i < len(ids):
    if i < len(ids) - 1 and ids[i] == pair[0] and ids[i+1] == pair[1]:
      newids.append(idx)
      i += 2
    else:
      newids.append(ids[i])
      i += 1
  return newids




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

def encode(raw_tokens, merges):
  while len(raw_tokens) >= 2:
    stats = get_stats(raw_tokens)
    pair = min(stats, key=lambda p: merges.get(p, float("inf")))
    print("pair", pair)
    if pair not in merges:
      break # nothing else can be merged
    idx = merges[pair]
    raw_tokens = merge(raw_tokens, pair, idx)
  return raw_tokens


test_dataset_fn = 'data/datasets_v1/20240301-2016/processed_examples/processed_examples.pkl'
with open(test_dataset_fn, 'rb') as f:
    test_dataset = pickle.load(f)
# flatten
test_dataset = [item for sublist in test_dataset for item in sublist]

encoded_test = encode(test_dataset, merges['merges'])
print(len(encoded_test))
