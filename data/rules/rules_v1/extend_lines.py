import numpy as np
import random

def generate_config():
    colors = random.sample(range(0, 9), 2)

    color_swap_random_config = {
        'description':  'random background color, random dots one color in input, swap to different color output',

        'nb_examples': 4,

        'min_height': 6,
        'max_height': 12,
        'min_width': 6,
        'max_width': 12,

        
        'line_color': colors[0],
        'background_color': colors[1]
    }

    return color_swap_random_config


def gex(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    input = np.ones((height, width)) * config['background_color']
    output = np.ones((height, width)) * config['background_color']

    x = random.randint(0, width-1)
    y = random.randint(0, height-1)

    input[y,x] = config['line_color']

    for r in range(height):
        for c in range(width):
            if r == y or c == x:
                output[r,c] = config['line_color']


    return input, output



def example_func():
    return gex