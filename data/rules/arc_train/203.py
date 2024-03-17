import numpy as np
import random

# ARC Public training set 117

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
    }

    return config




def generate_example(config):

    nb_colors = random.randint(2, 7)
    colors = random.sample(range(0, 9), nb_colors)
    dim = nb_colors * 2

    input = np.ones((dim, dim), dtype=int) * colors[0]
    output = np.ones((dim, dim), dtype=int) * colors[0]

    for i in range(nb_colors):
        margin = dim - i
        input[i:margin, i:margin] = colors[i]

        # output is the opposite
        output[i:margin, i:margin] = colors[nb_colors - i - 1]


    return input, output



def example_func():
    return generate_example