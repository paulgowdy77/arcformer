import numpy as np
import random



def color_swap_random_gex(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    input = np.ones((height, width)) * config['background_color']
    output = np.ones((height, width)) * config['background_color']

    for i in range(height):
        for j in range(width):
            if random.random() < 0.1:
                input[i, j] = config['input_color']
                output[i, j] = config['output_color']


    return input, output

def generate_config():
    colors = random.sample(range(0, 9), 3)

    color_swap_random_config = {
        'description':  'random background color, random dots one color in input, swap to different color output',

        'nb_examples': 4,

        'min_height': 4,
        'max_height': 8,
        'min_width': 4,
        'max_width': 8,

        
        'input_color': colors[0],
        'output_color': colors[1],
        'background_color': colors[2]
    }

    return color_swap_random_config

def example_func():
    return color_swap_random_gex