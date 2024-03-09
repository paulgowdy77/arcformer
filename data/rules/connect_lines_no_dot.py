import numpy as np
import random

def generate_config():
    config = {
    }
    return config

def generate_example(config):
    nb_lines = random.randint(1, 3)
    line_colors = random.sample(range(0, 9), 1 + nb_lines*2)

    half_width = random.choice([4,5,6,7])
    width = half_width * 2
    height = random.randint(6,10)

    input = np.ones((height, width)) * line_colors[0]
    output = input.copy()

    # place dots on the left and right edges of the input lined up
    for i in range(1, nb_lines*2, 2):
        y = random.randint(0, height-1)
        # make sure we're not overlapping dots
        while input[y, 0] == line_colors[i] or input[y, -1] == line_colors[i+1]:
            y = random.randint(0, height-1)
        input[y, 0] = line_colors[i]
        input[y, -1] = line_colors[i+1]

        # extend lines from the dots in the output
        output[y, :half_width] = line_colors[i]
        output[y, half_width:] = line_colors[i+1]

    # randomly rotate the input and output grids
    if random.random() > 0.5:
        input = np.rot90(input)
        output = np.rot90(output)
   
    return input, output



def example_func():
    return generate_example