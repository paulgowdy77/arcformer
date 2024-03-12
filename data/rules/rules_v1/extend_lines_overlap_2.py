import numpy as np
import random

def generate_config():
    colors = random.sample(range(0, 9), 5)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 10,
        'max_height': 18,
        'min_width': 10,
        'max_width': 18,

        'colors': colors,
        'nb_vert': random.randint(1, 3),
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

    # split colors into vertical and horizontal
    
    # vertical colors are used for vertical lines
    # horizontal colors are used for horizontal lines
    nb_vert = config['nb_vert']
    #nb_horiz = random.randint(1, 4 - nb_vert)

    #vert_colors = colors[1:nb_vert + 1]
    #horiz_colors = colors[nb_vert + 1:]

    vert_coords = random.sample(range(0, height), 4)
    horiz_coords = random.sample(range(0, width), 4)

    for i in range(4):
        input[vert_coords[i], horiz_coords[i]] = colors[i + 1]

        if (i+1) < nb_vert:
            output[vert_coords[i], :] = colors[i + 1]
        else:
            output[:, horiz_coords[i]] = colors[i + 1]
            

    
   


    return input, output



def example_func():
    return generate_example