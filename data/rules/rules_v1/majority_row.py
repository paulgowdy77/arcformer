import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 4,
        'max_height': 6,
        'min_width': 4,
        'max_width': 8,

        'rotate': random.randint(0,1)
    }

    return config


def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    colors = random.sample(range(0, 9), 6)

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    for i in range(height):
        for j in range(width):
            input[i,j] = colors[random.randint(0,5)]
        counts = [0,0,0,0,0,0]
        for j in range(width):
            #print(input[i,j])
            counts[colors.index(int(input[i,j]))] += 1
        if counts.count(max(counts)) != 1:
            for j in range(width):
                output[i,j] = input[i,j]
        else:
            for j in range(width):
                output[i,j] = colors[counts.index(max(counts))]


    


    return input, output



def example_func():
    return generate_example