import numpy as np
import random

# ARC Public eval set 81
# this is XOR
# NOTE: this is in rules_v1 so there will be overlap if I use arc_evaluation as a test set

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        'fixed_colors': random.sample(range(0, 9), 4),
    }

    return config


def generate_example(config):
    fixed_colors = config['fixed_colors']
    height = random.randint(4, 8)
    width = random.randint(4, 8)

    input = np.ones((height*2, width)) * fixed_colors[0]
    output = np.ones((height, width)) * fixed_colors[0]

    for r in range(height):
        for c in range(width):
            if random.random() > 0.5:
                input[r,c] = fixed_colors[1]
            if random.random() > 0.5:
                input[r+height,c] = fixed_colors[2]

            # implement xor here
            if input[r,c] == fixed_colors[1] and input[r+height,c] == fixed_colors[0]:
                output[r,c] = fixed_colors[3]
            elif input[r,c] == fixed_colors[0] and input[r+height,c] == fixed_colors[2]:
                output[r,c] = fixed_colors[3]


    return input, output



def example_func():
    return generate_example