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
        'max_width': 18,
    }

    return config


def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    colors = random.sample(range(0, 9), 3)

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    old_x = -1
    old_y = -1

    for i in range(2):

        x = random.randint(3, height-3)
        y = random.randint(3, width-3)

        while abs(x - old_x) < 3 or abs(y - old_y) < 3:
            x = random.randint(3, height-3)
            y = random.randint(3, width-3)


        input[x,y] = colors[1]
        input[x,y-1] = colors[2]
        input[x,y+1] = colors[2]
        input[x+1,y] = colors[2]
        input[x-1,y] = colors[2]

        output[x,y] = colors[1]

        output[x+1,y+1] = colors[2]
        output[x+2,y+2] = colors[2]
        output[x-1,y-1] = colors[2]
        output[x-2,y-2] = colors[2]

        output[x+1,y-1] = colors[2]
        output[x+2,y-2] = colors[2]
        output[x-1,y+1] = colors[2]
        output[x-2,y+2] = colors[2]


        output[x,y-2] = colors[1]
        output[x,y+2] = colors[1]
        output[x+2,y] = colors[1]
        output[x-2,y] = colors[1]
        output[x,y-1] = colors[1]
        output[x,y+1] = colors[1]
        output[x+1,y] = colors[1]
        output[x-1,y] = colors[1]

        old_x = x
        old_y = y


    return input, output



def example_func():
    return generate_example