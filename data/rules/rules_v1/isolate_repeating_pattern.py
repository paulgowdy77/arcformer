import numpy as np
import random

def generate_config():

    config = {
    }

    return config



def generate_example(config):
    pattern_height = random.randint(2, 5)
    pattern_width = random.randint(2, 5)

    pattern = np.ones((pattern_height, pattern_width))

    for i in range(pattern_height):
        for j in range(pattern_width):
            pattern[i, j] = random.randint(0, 9)

    output = pattern.copy()
    pattern_copy_number_x = random.randint(2, 4)
    pattern_copy_number_y = random.randint(1, 4)
    # tile pattern to make input
    input = np.tile(pattern, (pattern_copy_number_x, pattern_copy_number_y))

    # randomly flip the input and output
    if random.random() > 0.5:
        input = np.flip(input, 0)
        output = np.flip(output, 0)





    return input, output



def example_func():
    return generate_example