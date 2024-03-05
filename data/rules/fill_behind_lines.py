import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 14,
        'max_height': 20,
        'min_width': 6,
        'max_width': 8,
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

    start = random.randint(0, int(height/3))
    sides = [0,width-1]
    random.shuffle(sides)
    distance = random.choice([2,2,3,4])

    
    input[start,sides[0]] = colors[1]
    input[start+distance,sides[1]] = colors[2]


    for i in range(height):
        if i <= start:
            output[i,:] = colors[1]
        if i >= start+distance:
            output[i,:] = colors[2]


    if random.random() < 0.5:
        input = np.rot90(input, k=1)
        output = np.rot90(output, k=1)

    if random.random() <0.5:
        input = np.flipud(input)
        output = np.flipud(output)



    return input, output



def example_func():
    return generate_example