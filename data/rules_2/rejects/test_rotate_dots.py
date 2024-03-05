import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 5,

        'min_height': 8,
        'max_height': 16,
        'min_width': 8,
        'max_width': 12,
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
    output = np.ones((height, width)) * colors[0]

    nb_dots = random.randint(1,4)

    dot_verts = random.sample(range(0,height-1), nb_dots) 
    dot_horis = random.sample(range(0,width-1), nb_dots)

    for i in range(nb_dots):
        input[dot_verts[i], dot_horis[i]] = colors[1]
        output[dot_verts[i], dot_horis[i]] = colors[1]

    output = np.rot90(output, nb_dots)


    return input, output



def example_func():
    return generate_example