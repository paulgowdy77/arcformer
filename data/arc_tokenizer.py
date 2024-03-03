import pickle


class ArcTokenizer:
    def __init__(self, merge_pickle_file):

        with open(merge_pickle_file, 'rb') as f:
            vocab_and_merges = pickle.load(f)

        self.merges = vocab_and_merges['merges']
        self.initial_token_count = vocab_and_merges['token_count']