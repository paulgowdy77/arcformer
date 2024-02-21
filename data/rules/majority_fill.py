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

    input_matrix = np.zeros((height, width))
    output_matrix = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            if random.random() > 0.5:
                input_matrix[i, j] = 1
            else:
                input_matrix[i, j] = 0

    for i in range(height):
        for j in range(width):
            if random.random() > 0.5:
                output_matrix[i, j] = 1
            else:
                output_matrix[i, j] = 0

    example = (input_matrix, output_matrix)
    return example

def example_func():
    return generate_example