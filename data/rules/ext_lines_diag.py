import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  'random background color, random dots one color in input, swap to different color output',

        'nb_examples': 4,

        'min_height': 6,
        'max_height': 12,
        'min_width': 6,
        'max_width': 12,
    }

    return config


def gex(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    colors = random.sample(range(0, 9), 2)

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    # print(height, width)
    # print(y,x)
    # print("---")

    input[y,x] = colors[1]

    for r in range(height):
        for c in range(width):
            if r - y == c - x:
                output[r,c] = colors[1]

            if r - y == x - c:
               output[r,c] = colors[1] 


    return input, output



def example_func():
    return gex