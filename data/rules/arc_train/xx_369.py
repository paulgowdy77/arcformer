import numpy as np
import random

# ARC Public training set 368

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        "fixed_colors": random.sample(range(0, 9), 2)
    }

    return config


def generate_example(config):

    fixed_colors = config['fixed_colors']
    nb_colors = random.randint(2, 4)
    # sample colors not in fixed_colors
    colors = random.sample([c for c in range(9) if c not in fixed_colors], nb_colors)

    height = random.randint(10, 20)
    width = random.randint(10, 20)

    input = np.ones((height, width), dtype=int) * fixed_colors[0]
    output = np.ones((height, width), dtype=int) * fixed_colors[0]

    for i, color in enumerate(colors):
        spot_size = i+1

        # create spots of spot_size pixels that DO NOT touch any other dot
        for _ in range(spot_size):
            x = random.randint(0, width-1)
            y = random.randint(0, height-1)
            while input[y, x] != fixed_colors[0] or any([x < x2 + 2 and x + 2 > x2 and y < y2 + 2 and y + 2 > y2 for x2, y2 in zip(*np.where(input == color))]):
                x = random.randint(0, width-1)
                y = random.randint(0, height-1)
            input[y, x] = color


    return input, output



def example_func():
    return generate_example