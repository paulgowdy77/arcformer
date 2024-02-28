import numpy as np
import random

def generate_config():
    config = {
    
    }
    return config



def generate_example(config):

    colors = random.sample(range(0,9), 3)

    input = np.ones((16, 16)) * colors[0]

    # create 1 to 4 random large rectangles

    for i in range(random.randint(2, 4)):

        # random rectangle size
        rectangle_width = random.randint(4, 9)
        rectangle_height = random.randint(4, 9)

        # generate a rectangle in a random position in the input
        x = random.randint(1, 16 - rectangle_width)
        y = random.randint(1, 16 - rectangle_height)
        input[y:y+rectangle_height, x:x+rectangle_width] = colors[1]

    output = np.copy(input)

    # add a little noise to the input
    for i in range(16):
        for j in range(16):
            if random.random() < 0.05:
                input[i, j] = colors[2]
    

    return input, output

def example_func():
    return generate_example