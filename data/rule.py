class Rule:
    def __init__(self, config, example_func):
        self.config = config
        self.example_func = example_func

    def generate_example(self):
        # this doesnt handle linked examples
        # like what if the inputs are a series with one more square colored in each time
        # so potentially need to create the whole example set at once...
        i, o = self.example_func(self.config)
        example = {
            'input': i,
            'output': o
        }
        return example