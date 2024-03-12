import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,
        'rotate': random.randint(0, 1),
        #'bg_color': random.randint(0, 9),
        'colors': random.sample(range(0, 9), 3),
    }

    return config


def generate_example(config):
    colors = config['colors']

    height = 6
    width = 3

    input = np.ones((height, width)) * colors[2]
    output = np.ones((height + width, width)) * colors[2]

    for i in range(height):
        for j in range(width):
            if random.random() > 0.5:
                input[i,j] = colors[0]
                output[i,j] = colors[1]

                if i < 3:
                    output[i+6,j] = colors[1]

    if config['rotate'] == 1:
        input = np.rot90(input, 1)
        output = np.rot90(output, 1)    


    return input, output



def example_func():
    return generate_example