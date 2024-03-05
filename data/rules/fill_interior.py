import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',
        'fill_color': random.randint(0,9),
        'nb_examples': 4,

        'min_height': 12,
        'max_height': 14,
        'min_width': 12,
        'max_width': 14,
    }

    return config


def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)
    fill_color = config['fill_color']

    colors = random.sample(range(0, 9), 2)
    while fill_color in colors:
        colors = random.sample(range(0,9),2)

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]



    nb_nuclei = random.randint(2,5)

    for i in range(nb_nuclei):
        p = (random.randint(0, height-1), random.randint(1,width-1))
        output[p] = fill_color

    for _ in range(4):
        for i in range(1,height-1):
            for j in range(1,width-1):
                if output[i,j] == fill_color:
                    if random.random() > 0.7:
                        output[i-1,j] = fill_color
                    if random.random() > 0.7:
                        output[i+1,j] = fill_color
                    if random.random() > 0.7:
                        output[i,j-1] = fill_color
                    if random.random() > 0.7:
                        output[i,j+1] = fill_color

    for i in range(height):
        for j in range(width):
            if output[i,j] == fill_color:
                if output[i-1,j] == colors[0] and i > 0:
                    output[i-1,j] = colors[1]
                    input[i-1,j] = colors[1]
                if i < height-1 and output[i+1,j] == colors[0]:
                    output[i+1,j] = colors[1]
                    input[i+1,j] = colors[1]
                if output[i,j-1] == colors[0] and j > 0:
                    output[i,j-1] = colors[1]
                    input[i,j-1] = colors[1]
                if j < width-1 and output[i,j+1] == colors[0]:
                    output[i,j+1] = colors[1]
                    input[i,j+1] = colors[1]



    return input, output



def example_func():
    return generate_example