import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 5,
        'max_height': 10,
        'min_width': 5,
        'max_width': 10,
    }

    return config


def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height) * 2
    width = random.randint(min_width, max_width) * 2

    colors = random.sample(range(0, 9), 4)

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    for i in range(height):
        input[i, 0] = colors[1]
        input[i, width-1] = colors[2]

        output[i, 0] = colors[1]
        output[i, width-1] = colors[2]

    for i in range(1,width-1):
        for j in range(0,height):
            if random.random() < 0.1:

                input[j,i] = colors[3]
                
                if i < width/2:
                    output[j, i] = colors[1]
                else:
                    output[j,i] = colors[2]

    if random.random() > 0.5:
        input = np.rot90(input, k=1, axes=(0,1))
        output = np.rot90(output, k=1, axes=(0,1))


    return input, output



def example_func():
    return generate_example