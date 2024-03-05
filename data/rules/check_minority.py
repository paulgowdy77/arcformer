import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 8,
        'max_height': 16,
        'min_width': 8,
        'max_width': 16,
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

    count = 0

    for r in range(height):
        for c in range(width):
            if random.random() > 0.5:
                input[r,c] = colors[1]
                count += 1
    
    if count / (height*width) < 0.5:
        output = np.ones((1,1)) * colors[1]
    else:
        output = np.ones((1,1)) * colors[0]


    return input, output



def example_func():
    return generate_example