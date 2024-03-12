import numpy as np
import random

def generate_config():
    config = {
        "min_height": 10,
        "max_height": 16,
        "min_width": 10,
        "max_width": 16,

        "nb_examples": 4
    }
    return config

def generate_example(config):
    height = random.randint(config["min_height"], config["max_height"])
    width = random.randint(config["min_width"], config["max_width"])

    nb_colors = random.randint(2, 5)
    colors = random.sample(range(0,9), nb_colors+1)

    input = np.ones((height, width), dtype=int) * colors[0]

    color_counts = random.sample(range(1, 20), nb_colors)
    color_counts.sort()

    for i, cc in enumerate(color_counts):
        for j in range(cc):
            x = random.randint(0, width-1)
            y = random.randint(0, height-1)
            input[y, x] = colors[i+1]

    output = np.ones((height, width), dtype=int) * colors[-1]
    return input, output

def example_func():
    return generate_example