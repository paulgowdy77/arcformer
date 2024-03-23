import pickle 
import matplotlib.pyplot as plt
import glob

TARGET_VOCAB_SIZE = 256 # the desired final vocabulary size

dataset_name = 'train_set_1'

processed_document_files = glob.glob(f'data/datasets_v1/{dataset_name}/processed_documents/*.pkl')

all_documents = []
for file in processed_document_files[:]:
    with open(file, 'rb') as f:
        document_chunk = pickle.load(f)
        print("example set documents", len(document_chunk))
        for document in document_chunk:
            all_documents.append(document)


# print the length of all examples combined
print("Number of documents:", len(all_documents))

def get_stats(ids):
    counts = {}
    for pair in zip(ids, ids[1:]):
        counts[pair] = counts.get(pair, 0) + 1
    return counts

def get_stats_document(documents):
    counts = {}

    for document in documents:
        doc_counts = get_stats(document)

        for key in doc_counts:
            counts[key] = counts.get(key, 0) + doc_counts[key]

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

def apply_merge_documents(documents, pair, idx):
    new_documents = []

    for document in documents:
        new_document = merge(document, pair, idx)
        new_documents.append(new_document)

    return new_documents

def show_doc_lengths(documents, n=10):
    print("========================")
    for i in range(n):
        print(i, len(documents[i]))
    print("========================")

# token_count = max(all_examples) + 1
# num_merges = TARGET_VOCAB_SIZE - token_count 
# ids = list(all_examples) # copy so we don't destroy the original list

# collect_text_length = []

token_count = 15
num_merges = 40


merges = {} # (int, int) -> int
for i in range(num_merges):

    ##stats = get_stats(ids)
    doc_stats = get_stats_document(all_documents)


    pair = max(doc_stats, key=doc_stats.get)
    idx = token_count + i
    print(f"merging {pair} into a new token {idx}")


    ##ids = merge(ids, pair, idx)
    all_documents = apply_merge_documents(all_documents, pair, idx)

    # print("text length condensed:", len(ids))
    # collect_text_length.append(len(ids))
    # print("")

    merges[pair] = idx

    show_doc_lengths(all_documents)
    



# print("total pixels in all example sets:", len(all_examples))
# print("compressed dataset size:", len(ids))

# plt.figure()
# plt.plot(collect_text_length)
# plt.show()

# with open(f'data/datasets_v1/{date}/{date}_processed_examples_bpe_MERGES.pkl', 'wb') as f:
    # pickle.dump({
    #     "merges": merges,
    #     "initial_token_count": token_count,
    # }, f)