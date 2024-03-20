import numpy as np
import random

# ARC Public eval set 94
# stack colors

def generate_config():

    stack_order = [1,2,3,4]
    random.shuffle(stack_order)

    config = {
        'fixed_colors': random.sample(range(0, 9), 5),
        "stack_order": stack_order
    }

    return config


def generate_example(config):
    fixed_colors = config['fixed_colors']

    height = 4 * 4
    width = 6

    input = np.ones((height, width)) * fixed_colors[0]
    output = np.ones((4, width)) * fixed_colors[0]

    stack_order = config["stack_order"]

    for i in range(height):
        for j in range(width):
            if random.random() > 0.5:
                c_ind = 1 + i // 4
                input[i,j] = fixed_colors[c_ind]
   
    for stack_position in stack_order:
        for i in range(4):
            for j in range(width):
                if input[i + (stack_position - 1) * 4, j] != fixed_colors[0]:
                    output[i, j] = fixed_colors[stack_position]

    return input, output



def example_func():
    return generate_example