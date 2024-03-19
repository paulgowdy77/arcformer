import numpy as np
import random

# ARC Public training set 283

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        "fixed_colors": random.sample(range(0, 9), 5)
    }

    return config




def generate_example(config):

    colors = config["fixed_colors"]
    height = random.randint(12, 22)
    width = random.randint(12, 22)

    input = np.ones((height, width), dtype=int) * colors[0]
    output = np.ones((height, width), dtype=int) * colors[0]

    


    max_nb_rectangles = random.randint(2,5)

    placement_attempts = 0
    nb_rectangles = 0

    while placement_attempts < 50 and nb_rectangles < max_nb_rectangles:
        rect_width = random.randint(2, 6)
        rect_height = random.randint(2, 6)

        x = random.randint(0, width - rect_width)
        y = random.randint(0, height - rect_height)

        if np.any(input[y:y+rect_height, x:x+rect_width] != colors[0]):
            placement_attempts += 1
            continue

        input[y:y+rect_height, x:x+rect_width] = colors[1]

        # output has a unique pattern
        output[y, x] = colors[2]
        output[y, x+rect_width-1] = colors[2]
        output[y+rect_height-1, x] = colors[2]
        output[y+rect_height-1, x+rect_width-1] = colors[2]

        output[y+1:y+rect_height-1, x+1:x+rect_width-1] = colors[3]

        nb_rectangles += 1


    return input, output



def example_func():
    return generate_example