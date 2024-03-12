import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 4,
        'max_height': 5,
        'min_width': 4,
        'max_width': 5,

        'bg_color': random.randint(0,9)


    }

    return config


def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = 10#2*random.randint(min_height, max_height)
    width = 10#2*random.randint(min_width, max_width)


    colors = random.sample(range(0, 9), 3)
    while config['bg_color'] in colors:
        colors = random.sample(range(0, 9), 3)

    input = np.ones((height, width)) * config['bg_color']
    output = np.ones((height, width)) * config['bg_color']


    input_keeps = [[],[],[]]
    for i in range(height):
        if i % 3 == 0:
            input_keeps[0].append(i)
        if i % 3 == 1:
            input_keeps[1].append(i)
        if i % 3 == 2:
            input_keeps[2].append(i)

        for j in range(width):
            if ((i*width)+j) % 3 == 0:
                output[i,j] = colors[0]
            if ((i*width)+j) % 3 == 1:
                output[i,j] = colors[1]
            if ((i*width)+j) % 3 == 2:
                output[i,j] = colors[2]

    keeps = [random.choice(input_keeps[0]), random.choice(input_keeps[1]), random.choice(input_keeps[2])]

    for c, k in enumerate(keeps):
        for i in range(k+1):
            input[k - i, i] = colors[c]


    return input, output



def example_func():
    return generate_example