import pickle


class ArcTokenizer:
    def __init__(self, merge_pickle_file):

        with open(merge_pickle_file, 'rb') as f:
            vocab_and_merges = pickle.load(f)

        self.merges = vocab_and_merges['merges']
        self.initial_token_count = vocab_and_merges['token_count']

        self.vocab = {idx: idx for idx in range(self.initial_token_count)}
        for (p0, p1), idx in self.merges.items():
            # flattened list
            new = []
            if type(self.vocab[p0]) == int:
                new.append(self.vocab[p0])
            else:
                for e in self.vocab[p0]:
                    new.append(e)
            if type(self.vocab[p1]) == int:
                new.append(self.vocab[p1])
            else:
                for e in self.vocab[p1]:
                    new.append(e)
            self.vocab[idx] = new

    def get_stats(self, ids):
        counts = {}
        for pair in zip(ids, ids[1:]):
            counts[pair] = counts.get(pair, 0) + 1
        return counts

    def merge(self, ids, pair, idx):
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
    

    def decode(self, tokens):
        decoded = []
        for token in tokens:
            if type(self.vocab[token]) == int:
                decoded.append(self.vocab[token])
            else:
                decoded.extend(self.vocab[token])
        return decoded

    def encode(self, raw_tokens):
        while len(raw_tokens) >= 2:
            stats = self.get_stats(raw_tokens)
            pair = min(stats, key=lambda p: self.merges.get(p, float("inf")))
            if pair not in self.merges:
                break # nothing else can be merged
            idx = self.merges[pair]
            raw_tokens = self.merge(raw_tokens, pair, idx)
        return raw_tokens