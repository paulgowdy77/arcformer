import numpy as np
import random

# ARC Public training set 241

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        'flip_dir': random.choice(['ud', 'lr'])
    }

    return config




def generate_example(config):

    nb_colors = random.randint(2, 7)
    colors = random.sample(range(0, 9), nb_colors)

    dim = random.randint(4,10)
    input = np.ones((dim, dim), dtype=int) * colors[0]

    for i in range(dim):
        for j in range(dim):
            if random.random() > 0.15:
                input[i, j] = random.choice(colors)

    if config['flip_dir'] == 'ud':
        output = np.flipud(np.rot90(input))
    else:
        output = np.fliplr(np.rot90(input))

    return input, output



def example_func():
    return generate_example