import pickle 
import matplotlib.pyplot as plt

date = '20240301-2016'

with open(f'data/datasets_v1/{date}/processed_examples/processed_examples.pkl', 'rb') as f:
    example_sets = pickle.load(f)

# join the example sets into a single list
all_examples = []
for example_set in example_sets:
    all_examples.extend(example_set)

# print the length of all examples combined
print("Number of example sets:", len(example_sets))
print("total pixels in all example sets:", sum([len(example_set) for example_set in example_sets]))

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

token_count = max(all_examples) + 1
target_vocab_size = 256 # the desired final vocabulary size
num_merges = target_vocab_size - token_count 
ids = list(all_examples) # copy so we don't destroy the original list

collect_text_length = []

merges = {} # (int, int) -> int
for i in range(num_merges):
    stats = get_stats(ids)
    pair = max(stats, key=stats.get)
    idx = token_count + i
    print(f"merging {pair} into a new token {idx}")
    ids = merge(ids, pair, idx)
    print("text length condensed:", len(ids))
    collect_text_length.append(len(ids))
    print("")
    merges[pair] = idx

print("total pixels in all example sets:", sum([len(example_set) for example_set in example_sets]))
print("final vocabulary size:", len(ids))

plt.figure()
plt.plot(collect_text_length)
plt.show()

with open(f'data/datasets_v1/{date}/processed_examples_bpe_MERGES.pkl', 'wb') as f:
    pickle.dump({
        "merges": merges,
        "token_count": token_count,
    }, f)