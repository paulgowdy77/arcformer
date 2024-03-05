import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'colors': random.sample(range(0,9), 8),

        'rotate': random.randint(0,1)

    }

    return config


def generate_example(config):
   
    colors = config['colors']

    input = np.ones((3, 3))
    output = np.ones((3, 3))

    color_order = random.sample(range(0,4),3)

    for i in range(3):
        input[:,i] = colors[color_order[i]]
        output[:,i] = colors[color_order[i]+4]

    if config['rotate'] > 0:
        np.rot90(input, 1, (1,0))
        np.rot90(output, 1, (1,0))


    return input, output



def example_func():
    return generate_example