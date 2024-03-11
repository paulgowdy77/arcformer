import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    fixed_colors = random.sample(range(0, 9), 2)

    config = {
        'fixed_colors': fixed_colors,
    }

    return config


def generate_example(config):

    fixed_colors = config['fixed_colors']
    # generate two colors not in fixed_colors
    colors = random.sample([x for x in range(0,9) if x not in fixed_colors], 1)

    height = random.randint(6, 10)
    width = random.randint(6, 10)

    input = np.ones((height, width)) * fixed_colors[0]
    output = np.ones((height, width)) * fixed_colors[0]

    for c in range(width):
        # get a height for the lock
        lock_height = random.randint(1, height-1)
        # get a height for the key
        key_height = height - lock_height

        input[:lock_height, c] = colors[0]
        output[lock_height:, c] = fixed_colors[1]

    

   


    return input, output



def example_func():
    return generate_example