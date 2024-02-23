import numpy as np
import random

def generate_config():
    config = {
    
    }
    return config



def generate_example(config):

    colors = random.sample(range(0,9), 2)

    input = np.ones((12, 12)) * colors[0]
    output = np.ones((12, 12)) * colors[0]

    # generate a 2x2 square in a random position in the input
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    input[y, x] = colors[1]
    input[y+1, x] = colors[1]
    input[y, x+1] = colors[1]
    input[y+1, x+1] = colors[1]
    

    return input, output

def example_func():
    return generate_example