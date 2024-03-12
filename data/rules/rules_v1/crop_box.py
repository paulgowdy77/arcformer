import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 14,
        'max_height': 18,
        'min_width': 14,
        'max_width': 20,
    }

    return config


def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    colors = random.sample(range(0, 9), 5)

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    for i in range(height):
        for j in range(width):
            x = random.randint(0,3)
            input[i,j] = colors[x]

    crop_height = random.randint(4,10)
    crop_width = random.randint(4,10)

    crop_x = random.randint(0, width - crop_width - 1)
    crop_y = random.randint(0, height - crop_height - 1)

    for i in range(crop_height):
        input[crop_y + i, crop_x] = colors[-1]
        input[crop_y + i, crop_x + crop_width - 1] = colors[-1]
    for j in range(crop_width):
        input[crop_y, crop_x + j] = colors[-1]
        input[crop_y + crop_height - 1, crop_x + j] = colors[-1]

    output = input[crop_y + 1:crop_y + crop_height - 1, crop_x + 1:crop_x + crop_width - 1]



    return input, output



def example_func():
    return generate_example