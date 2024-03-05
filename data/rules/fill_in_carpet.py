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

        'colors': random.sample(range(0, 9), 7)
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
    output = np.ones((height, width))  * colors[0]


    mods = random.sample([2,2,2,3,3,3,4,4,5,5,2,2,2], 7)

    for i in range(height):
        for j in range(width):

            if (i + j) % mods[0] == 0:
                input[i,j] = colors[1]
                output[i,j] = colors[1]
            if (i + j+1) % mods[1] == 0:
                input[i,j] = colors[2]
                output[i,j] = colors[2]
            # if (i + j+1) % mods[2] == 0:
            #     input[i,j] = colors[3]
            #     output[i,j] = colors[3]
            if (i + j) % mods[3] == 0:
                input[i,j] = colors[3]
                output[i,j] = colors[3]

            if i % mods[4] == 1 and j % mods[5] == 0:
                input[i,j] = colors[4]
                output[i,j] = colors[4]

            # if i % mods[6] == 0 and j % 2 == 1:
            #     input[i,j] = colors[5]

    

    for i in range(random.randint(1,3)):

        _height = random.randint(2,5)
        _width = random.randint(2,5)

        top_left = (random.randint(0,height - _height), random.randint(0,width - _width))

        input[top_left[0]:top_left[0]+_height,top_left[1]:top_left[1]+_width] = np.ones((_height,_width))*colors[-1]
        


    return input, output



def example_func():
    return generate_example