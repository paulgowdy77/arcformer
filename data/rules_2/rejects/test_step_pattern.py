import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': random.randint(4,5),

        'min_height': 16,
        'max_height': 18,
        'min_width': 14,
        'max_width': 20,

        'up': random.randint(0,1),
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

    step_height = random.randint(1,3)
    #step_start = random.randint(1,5)

    for i in range(int(width/2)):
        input[:i*step_height, i] = colors[1]
        output[:i*step_height, i] = colors[1]

    for i in range(int(width/2),width):
        #input[:i*step_height, i] = colors[1]
        output[:i*step_height, i] = colors[1]
   


    return input, output



def example_func():
    return generate_example