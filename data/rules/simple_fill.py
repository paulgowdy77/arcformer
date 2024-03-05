import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 3,

        'min_height': 4,
        'max_height': 6,
        'min_width': 6,
        'max_width': 6,
    }
    return config


def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    colors = random.sample(range(0, 9), 2)

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[1]

    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    input[y,x] = colors[1]


    return input, output



def example_func():
    return generate_example