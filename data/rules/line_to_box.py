import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 5,
        'max_height': 8,
        'min_width': 8,
        'max_width': 14,

        'flip': random.randint(0,1)
    }

    return config


def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height) * 2
    width = random.randint(min_width, max_width)

    colors = random.sample(range(0, 9), 3)

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    top_margin = random.randint(1,3)
    bottom_margin = random.randint(1,3)

    top_coord = random.randint(1,width-2)
    bottom_coord = random.randint(1,width-2)

    input[1+top_margin, top_coord] = colors[1]
    input[height-2-bottom_margin, bottom_coord] = colors[2]

    output[0,:] = colors[1]
    output[height-1,:] = colors[2]
    output[:int(height/2),0] = colors[1]
    output[:int(height/2),width-1] = colors[1]
    output[int(height/2):,0] = colors[2]
    output[int(height/2):,width-1] = colors[2]
    output[height-2-bottom_margin,:] = colors[2]
    output[1+top_margin,:] = colors[1]

    if config['flip'] == 1:
        input = np.rot90(input,1)
        output = np.rot90(output,1)


    return input, output



def example_func():
    return generate_example