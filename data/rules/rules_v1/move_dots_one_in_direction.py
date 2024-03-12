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

        # move the dots in the direction specified in the config
        if direction == "up":
            output[y-1, x] = input[y, x]
        elif direction == "down":
            output[y+1, x] = input[y, x]
        elif direction == "left":
            output[y, x-1] = input[y, x]
        elif direction == "right":
            output[y, x+1] = input[y, x]


    return input, output

def example_func():
    return generate_example