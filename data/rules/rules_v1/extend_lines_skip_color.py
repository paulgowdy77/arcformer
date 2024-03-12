import numpy as np
import random

def generate_config():

    config = {
        'fixed_colors': random.sample(range(0, 9), 2),
 
    }

    return config


def generate_example(config):

    fixed_colors = config['fixed_colors']
    # get all other colors not in fixed_colors
    other_colors = [i for i in range(9) if i not in fixed_colors]

    height = random.randint(16, 22)
    width = random.randint(16, 22)

    input = np.ones((height, width)) * fixed_colors[0]

    # carpet the whole input with other colors
    for i in range(height):
        for j in range(width):
            input[i, j] = random.choice(other_colors)

            if random.random() > 0.9:
                input[i, j] = fixed_colors[1]

    output = input.copy()
    bar_width = random.randint(1, 3)

    # create blocks of fixed_colors[0] in the input and output

    block_x = random.randint(4, width - bar_width - 4)
    block_y = random.randint(4, height - bar_width - 4)

    input[block_y:block_y + bar_width, block_x:block_x + bar_width] = fixed_colors[0]
    output[block_y:block_y + bar_width, block_x:block_x + bar_width] = fixed_colors[0]

    # extend the block to the edges of the output horizontally and vertically
    for i in range(height):
        for w in range(bar_width):
            if output[i, block_x + w] != fixed_colors[1]:
                output[i, block_x + w] = fixed_colors[0]

    for j in range(width):
        for w in range(bar_width):
            if output[block_y + w, j] != fixed_colors[1]:
                output[block_y + w, j] = fixed_colors[0]

 
    return input, output



def example_func():
    return generate_example