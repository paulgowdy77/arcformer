import numpy as np
import random

def generate_config():
    config = {
        "direction": random.choice(["up", "down", "left", "right"])
    }
    return config



def generate_example(config):
    nb_colors = random.randint(2, 5)
    colors = random.sample(range(0,9), nb_colors)

    input = np.ones((12, 12)) * colors[0]
    output = np.ones((12, 12)) * colors[0]

    direction = config["direction"]
    # generate colored dots in random positions
    for i in range(10):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        input[y, x] = random.choice(colors[1:])
        output[y, x] = input[y, x]

    # move the dots in the direction specified in the config
    # until they hit the edge of the grid
    # or another dot
    # need to iterate over the grid in the opposite direction of the movement
    # to avoid overwriting the dots
    # only move the dots in the output
        
    # move the dots until they hit the edge of the grid
    # or another dot
        
    if direction == "up":
        for y in range(1, 11):
            for x in range(1, 11):
                while output[y, x] != 1 and output[y-1, x] == 1:
                    output[y-1, x] = output[y, x]
                    output[y, x] = 1


    return input, output

def example_func():
    return generate_example