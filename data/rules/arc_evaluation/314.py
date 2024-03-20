import numpy as np
import random

# ARC Public eval set 314
# color symetric

def generate_config():

    config = {
        "fixed_colors": random.sample(range(0, 9), 3)
    }

    return config


def generate_example(config):

    colors = config['fixed_colors']

    height = random.randint(8, 18)
    width = 2 * random.randint(4, 9)

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    for i in range(height):
        for j in range(width):
            if random.random() > 0.65:
                input[i,j] = colors[1] 
                output[i,j] = colors[1] 

    # color symetric with colors[2]
    for i in range(height):
        for j in range(width//2):
            if input[i,j] == colors[1] and input[i,width-1-j] == colors[1]:

                output[i,width-1-j] = colors[2]
                output[i,j] = colors[2]

    return input, output



def example_func():
    return generate_example