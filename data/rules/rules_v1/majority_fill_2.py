import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 12,
        'max_height': 16,
        'min_width': 12,
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

    nb_colors = random.randint(2, 5)
    colors = random.sample(range(0, 9), nb_colors + 1)

    input = np.ones((height, width)) * colors[0]
    color_dots = colors[1:]

    color_counts = random.sample(range(0, 30), nb_colors)
    color_counts.sort()

    for i, cc in enumerate(color_counts):
        for j in range(cc):
            x = random.randint(0, width-1)
            y = random.randint(0, height-1)
            input[y,x] = color_dots[i]

    output = np.ones((height, width)) * color_dots[-1]

    return input, output



def example_func():
    return generate_example