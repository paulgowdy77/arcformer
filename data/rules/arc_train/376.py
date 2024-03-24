import numpy as np
import random

# ARC Public training set 376

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
    }

    return config


def generate_example(config):

    colors = random.sample(range(0, 9), 4)

    width = random.randint(10, 18)
    height = random.randint(4, 8)

    input = np.ones((height, width), dtype=int) * colors[0]

    for i in range(height):
        for j in range(width):
            input[i, j] = random.choice(colors)

    output = np.zeros((height*4, width), dtype=int)
    output[:height, :] = input
    output[height:height*2, :] = np.flipud(input)
    output[height*2:height*3, :] = np.flipud(np.flipud(input))
    output[height*3:, :] = np.flipud(np.flipud(np.flipud(input)))

    
    

    return input, output



def example_func():
    return generate_example