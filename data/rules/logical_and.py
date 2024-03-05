import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,
        'colors' : random.sample(range(0, 9), 4)

        # 'min_height': 6,
        # 'max_height': 12,
        # 'min_width': 6,
        # 'max_width': 12,
    }

    return config

def generate_stamp(bg_color, shape_color):
    stamp = np.ones((3,3)) * bg_color
    for i in range(3):
        for j in range(3):
            if random.random() > 0.45:
                stamp[i,j] = shape_color
    return stamp


def generate_example(config):


    colors = config['colors']

    input = np.ones((3, 7)) * colors[0]
    output = np.ones((3,3)) * colors[0]

    input[:,3] = colors[1]

    s1 = generate_stamp(colors[0], colors[2])
    s2 = generate_stamp(colors[0], colors[2])

    input[0:3,0:3] = s1
    input[0:3,4:7] = s2

    for i in range(3):
        for j in range(3):
            if s1[i,j] == colors[2] and s2[i,j] == colors[2]:
                output[i,j] = colors[3]

    return input, output



def example_func():
    return generate_example