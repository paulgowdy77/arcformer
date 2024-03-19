import numpy as np
import random

# ARC Public training set 87
# rotate input X time

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        'nb_rotations': random.randint(1, 3)
    }

    return config


def generate_example(config):

    dim = random.randint(3, 7)

    colors = random.sample(range(0, 9), 6)
    input = np.ones((dim, dim), dtype=int) * colors[0]

    for i in range(dim):
        for j in range(dim):
            if random.random() > 0.15:
                input[i, j] = random.choice(colors)

    output = np.rot90(input, k=config['nb_rotations'])
    

    return input, output



def example_func():
    return generate_example