import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 8,
        'max_height': 12,
        'min_width': 12,
        'max_width': 16,

        'rotate': random.randint(0,1)
    }

    return config


def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    colors = random.sample(range(0, 9), 6)

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    for i in range(height):
        for j in range(width):
            input[i,j] = colors[random.randint(0,4)]

    r = random.randint(0,height-1)

    for j in range(width):
        input[r,j] = colors[-1]

    for j in range(width):
        output[:,j] = input[:,0]

    if config['rotate'] > 0:
        input = np.rot90(input, k=1, axes=(0,1))
        output = np.rot90(output, k=1, axes=(0,1))


    return input, output



def example_func():
    return generate_example