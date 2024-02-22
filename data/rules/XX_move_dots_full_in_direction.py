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
        if direction == "up":
            while output[y-1, x] == colors[0] and y > 0:
                output[y-1, x] = output[y, x]
                output[y, x] = colors[0]
                y -= 1
        elif direction == "down":
            while output[y+1, x] == colors[0] and y < 10:
                output[y+1, x] = output[y, x]
                output[y, x] = colors[0]
                y += 1
        elif direction == "left":
            while output[y, x-1] == colors[0] and x > 0:
                output[y, x-1] = output[y, x]
                output[y, x] = colors[0]
                x -= 1
        elif direction == "right":
            while output[y, x+1] == colors[0] and x < 10:
                output[y, x+1] = output[y, x]
                output[y, x] = colors[0]
                x += 1


    return input, output

def example_func():
    return generate_example