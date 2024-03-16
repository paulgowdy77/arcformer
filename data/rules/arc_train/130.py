import numpy as np
import random

# ARC Public training set 33

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
    }

    return config


def generate_example(config):

    colors = random.sample(range(0, 9), 2)
    other_colors = random.sample([x for x in range(9) if x not in colors], 6)

    output = np.ones((3, 3), dtype=int) * colors[0]
    input = np.ones((9, 9), dtype=int) * colors[0]

    for i in range(3):
        for j in range(3):
            if random.random() < 0.45:
                output[i, j] = random.choice(other_colors)

                input[i*3:i*3+3, j*3:j*3+3] = output[i, j]

    # add some noise
    for i in range(9):
        for j in range(9):
            if random.random() < 0.1:
                input[i, j] = colors[1]
    

    return input, output



def example_func():
    return generate_example