import numpy as np
import random

def generate_config():
    config = {
    
    }
    return config



def generate_example(config):

    colors = random.sample(range(0,9), 5)
    height = random.randint(2, 4)
    width = random.randint(2, 4)

    input = np.ones((height, width)) * colors[0]

    # put random color dots
    for i in range(height):
        for j in range(width):
            if random.random() < 0.5:
                input[i, j] = random.choice(colors[1:])
    
    # expand each cell in the input into a 2x2 square to make the output
    output = np.zeros((height*2, width*2))
    for i in range(height):
        for j in range(width):
            output[i*2:i*2+2, j*2:j*2+2] = input[i, j]
    



   
    return input, output

def example_func():
    return generate_example