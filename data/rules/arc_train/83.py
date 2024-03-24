import numpy as np
import random

# ARC Public training set 83
# mirror x4
# I feel like I've made this rule before - is it a duplicate?

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
    }

    return config


def generate_example(config):

    colors = random.sample(range(0, 9), 4)

    width = random.randint(4, 8)
    height = random.randint(4, 8)

    input = np.ones((height, width), dtype=int) * colors[0]

    for i in range(height):
        for j in range(width):
            input[i, j] = random.choice(colors)

    output = np.zeros((height*2, width*2), dtype=int)
    output[:height, :width] = input
    output[height:, :width] = np.flipud(input)
    output[:height, width:] = np.fliplr(input)
    output[height:, width:] = np.flipud(np.fliplr(input))

    
    

    return input, output



def example_func():
    return generate_example