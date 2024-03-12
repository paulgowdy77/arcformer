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
        'max_width': 6,

        'colors': random.sample(range(0, 9), 5),
    }

    return config


def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    colors = config['colors']
    off_color_ind = random.randint(2,4)

    input = np.ones((height, width)) * colors[0]
    #output = np.ones((height, width)) * colors[0]

    old_x = -2
    old_y = -2
    for i in range(random.randint(1,2)):
        x = random.randint(0, height-1)
        y = random.randint(0, width-1)
        while abs(x-old_x) < 2 or abs(y-old_y) < 2:
            x = random.randint(0, height-1)
            y = random.randint(0, width-1)

        input[x,y] = colors[off_color_ind]
        old_x = x
        old_y = y

    output = np.ones((height*2, width*2)) * colors[0]
    output[:height,:width] = input[:,:]
    output[height:,width:] = input[:,:]
    output[height:,:width] = input[:,:]
    output[:height,width:] = input[:,:]

    for i in range(height*2):
        for j in range(width*2):
            if output[i,j] == colors[off_color_ind]:
                if i < height*2-1 and j < width*2 - 1:
                    output[i+1,j+1] = colors[1]
                if i < height*2-1 and j > 0:
                    output[i+1,j-1] = colors[1]
                if i > 0 and j < width*2 - 1:
                    output[i-1,j+1] = colors[1]
                if i >0 and j >0:
                    output[i-1,j-1] = colors[1]


    return input, output



def example_func():
    return generate_example