import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

        # 'min_height': 14,
        # 'max_height': 18,
        # 'min_width': 14,
        # 'max_width': 20,
    }

    return config


def generate_example(config):
    # # min_height = config['min_height']
    # # max_height = config['max_height']
    # # min_width = config['min_width']
    # # max_width = config['max_width']

    # height = random.randint(min_height, max_height)
    # width = random.randint(min_width, max_width)

    colors = random.sample(range(0, 9), 5)

    input = np.ones((20, 12)) * colors[0]
    output = np.ones((20, 12)) * colors[0]

    for i in range(10,20):
        for j in range(12):
            x = random.randint(1,4)
            input[i,j] = colors[x]
            output[i,j] = colors[x]

    crop_height = random.randint(6,8)
    crop_width = random.randint(6,8)

    crop_x = random.randint(0, 10 - crop_width - 1)
    crop_y = random.randint(0, 10 - crop_height - 1)

    for i in range(crop_height):
        output[10 + crop_y + i, crop_x] = colors[0]
        output[10 + crop_y + i, crop_x + crop_width - 1] = colors[0]
    for j in range(crop_width):
        output[10 + crop_y, crop_x + j] = colors[0]
        output[10 + crop_y + crop_height - 1, crop_x + j] = colors[0]

    input[:crop_height,:crop_width] = output[10 + crop_y:10 + crop_y + crop_height, crop_x:crop_x + crop_width]
    output[:crop_height,:crop_width] = output[10 + crop_y:10 + crop_y + crop_height, crop_x:crop_x + crop_width]
   



    return input, output



def example_func():
    return generate_example