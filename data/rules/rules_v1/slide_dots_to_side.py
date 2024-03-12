import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)
    side_to_slide = random.choice([0, 1, 2, 3])

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 6,
        'max_height': 8,
        'min_width': 8,
        'max_width': 12,

        'slide_direction': side_to_slide
    }

    return config


def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    colors = random.sample(range(0, 9), 5)

    cols = random.sample(range(0, width), 4)
    cols.sort()

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    for i in range(4):
        output_stack_height = 0
        for j in range(height):
            if random.random() < 0.2:
                input[j, cols[i]] = colors[i+1]
                output[height - output_stack_height - 1, cols[i]] = colors[i+1]
                output_stack_height += 1

    nb_rotation = config['slide_direction']
    input = np.rot90(input, k=nb_rotation, axes=(0,1))
    output = np.rot90(output, k=nb_rotation, axes=(0,1))

    return input, output



def example_func():
    return generate_example