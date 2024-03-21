import numpy as np
import random

# ARC Public eval set 116
# color sudoku

def generate_config():

    config = {
        "nb_colors": random.randint(3, 6),
    }

    return config


def generate_example(config):

    nb_colors = config["nb_colors"]
    colors = random.sample(range(0, 9), nb_colors)

    input = np.ones((nb_colors, nb_colors))
    output = np.zeros((nb_colors, nb_colors))

    for i in range(nb_colors):
        for j in range(nb_colors):
            input[i, j] = (i + j) % nb_colors
            output[i, j] = (i + j + 1) % nb_colors

    
    return input, output



def example_func():
    return generate_example