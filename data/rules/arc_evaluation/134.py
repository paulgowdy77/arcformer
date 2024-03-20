import numpy as np
import random

# ARC Public eval set 134
# color columns

def generate_config():

    config = {
        "fixed_colors": random.sample(range(0, 9), 6),

        "rotate": random.random() > 0.5
    }

    return config


def generate_example(config):

    fixed_colors = config["fixed_colors"]
    bg_color = fixed_colors[0]
    hole_color = fixed_colors[1]
    bar_colors = fixed_colors[2:]

    height = random.randint(8, 14)
    width = random.randint(8, 14)

    input = np.ones((height, width)) * bg_color
    output = np.ones((height, width)) * bg_color

    bar_positions = random.sample(range(0, width), 4)
    bar_positions.sort()

    for i, x in enumerate(bar_positions):
        for y in range(height):
            
            if random.random() > 0.65:
                input[y, x] = hole_color
                output[y, x] = bar_colors[i]

    if config["rotate"]:
        input = np.rot90(input)
        output = np.rot90(output)

    
    return input, output



def example_func():
    return generate_example