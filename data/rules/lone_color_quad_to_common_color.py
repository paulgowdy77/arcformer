import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 18,
        'max_height': 24,
        'min_width': 18,
        'max_width': 24,
    }

    return config

def generate_quadrant(width, height, bg_color, color):
    quadrant = np.ones((height, width)) * bg_color
    for i in range(height):
        for j in range(width):
            if random.random() > 0.35:
                quadrant[i,j] = color
    return quadrant

def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    colors = random.sample(range(0, 9), 3)

    input = np.ones((height, width)) * colors[0]
    #output = np.ones((height, width)) * colors[0]

    width_1 = random.randint(6,9)
    channel_width = random.randint(2,4)
    width_2 = width - width_1 - channel_width

    height_1 = random.randint(6,9)
    channel_height = random.randint(2,4)
    height_2 = height - height_1 - channel_height

    diff_index = random.randint(0,3)

    colorz = [1,1,1,1]
    colorz[diff_index] = 2

    a = generate_quadrant(width_1, height_1, colors[0], colors[colorz[0]])
    input[0:height_1,0:width_1] = a

    b = generate_quadrant(width_2, height_1, colors[0], colors[colorz[1]])
    input[0:height_1,width_1+channel_width:] = b

    c = generate_quadrant(width_1, height_2, colors[0], colors[colorz[2]])
    input[height_1+channel_height:,0:width_1] = c

    d = generate_quadrant(width_2, height_2, colors[0], colors[colorz[3]])
    input[height_1+channel_height:,width_1+channel_width:] = d

    quads = [a,b,c,d]
    output = quads[diff_index]

    for i in range(output.shape[0]):
        for j in range(output.shape[1]):
            if output[i,j] == colors[2]:
                output[i,j] = colors[1]


    return input, output



def example_func():
    return generate_example