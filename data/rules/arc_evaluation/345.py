import numpy as np
import random

# ARC Public eval set 345

def generate_config():

    config = {
        "fixed_colors": random.sample(range(0, 9), 4)
    }

    return config


def generate_example(config):

    colors = config['fixed_colors']

    height = random.randint(4, 5)
    half_width = random.randint(3, 5)
    width = 2 * half_width

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, half_width)) * colors[0]

    for i in range(height):
        for j in range(half_width):
            if random.random() > 0.65:
                input[i,j] = colors[1]

        for j in range(half_width):
            if random.random() > 0.5:
                input[i,j+half_width] = colors[2]

    for i in range(height):
        for j in range(half_width):
            if input[i,j] == colors[0] and input[i,j+half_width] == colors[0]:
                output[i,j] = colors[3]

    return input, output



def example_func():
    return generate_example