import numpy as np
import random

def generate_config():
    colors = random.sample(range(0, 9), 6)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 12,
        'max_height': 16,
        'min_width': 12,
        'max_width': 16,

        'colors': colors,

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

    colors = config['colors']   

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    verts = random.sample(range(0, width-1), 4)
    verts.sort()

    for kk, v in enumerate(verts):
        for i in range(height):
            if random.random() > 0.5:
                input[i, v] = colors[1]
                output[i, v] = colors[2+kk]

    if config['rotate'] == 1:
        input = np.rot90(input,1)
        output = np.rot90(output,1)



    return input, output



def example_func():
    return generate_example