import numpy as np
import random

def generate_config():
    config = {
    
    }
    return config



def generate_example(config):

    colors = random.sample(range(0,9), 2)
    height = random.randint(6, 18)
    width = random.randint(6, 18)

    input = np.ones((height, width)) * colors[0]

    dot_count = 0
    for i in range(height):
        for j in range(width):
            if random.random() < 0.5:
                input[i, j] = colors[1]
                dot_count += 1
    
    if dot_count > (height * width) / 2:
        output = np.ones((height, width)) * colors[1]
    else:
        output = np.ones((height, width)) * colors[0]



   
    return input, output

def example_func():
    return generate_example