import numpy as np
import random

def generate_config():
    config = {
    
    }
    return config



def generate_example(config):

    colors = random.sample(range(0,9), 2)

    input = np.ones((16, 16)) * colors[0]
    #output = np.ones((16, 16)) * colors[1]

    # random square size
    square_size = random.randint(2, 7)

    # generate a square in a random position in the input
    x = random.randint(1, 16 - square_size)
    y = random.randint(1, 16 - square_size)
    input[y:y+square_size, x:x+square_size] = colors[1]

    output = np.ones((square_size, square_size)) * colors[0]
    

    return input, output

def example_func():
    return generate_example