import numpy as np
import random

# ARC Public training set 322

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        'nb_rotations': random.randint(0, 3)
    }

    return config




def generate_example(config):

    colors = random.sample(range(0, 9), 6)

    dim = random.randint(3,5)
    input = np.ones((dim, dim), dtype=int) * colors[0]
    output = np.ones((dim, dim), dtype=int) * colors[0]

    for i in range(dim):
        height = random.randint(0, dim-1)

        input[i, height] = colors[i+1]
        output[i, :height+1] = colors[i+1]

    
    nb_rotations = config['nb_rotations']
    input = np.rot90(input, nb_rotations)
    output = np.rot90(output, nb_rotations)

    return input, output



def example_func():
    return generate_example