import numpy as np
import random

# ARC Public training set 132

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
    }

    return config


def generate_example(config):

    colors = random.sample(range(0, 9), 5)
    height = random.randint(12, 20)
    width = random.randint(12, 20)

    input = np.ones((height, width), dtype=int) * colors[0]
    output = np.ones((height, width), dtype=int) * colors[0]

    # place non overlapping rectangles
    nb_rectangles = random.randint(1, 4)
    for i in range(nb_rectangles):
        rect_height = random.randint(2, 6)
        rect_width = random.randint(2, 6)

        x = random.randint(0, width - rect_width)
        y = random.randint(0, height - rect_height)

        overlapping = True
        while overlapping:
            if np.any(output[y:y+rect_height, x:x+rect_width] != colors[0]):
                x = random.randint(0, width - rect_width)
                y = random.randint(0, height - rect_height)
            else:
                overlapping = False
        output[y:y+rect_height, x:x+rect_width] = colors[i+1]
        
        if random.random() > 0.5:
            # make top left and bottom right corners colored in the input
            input[y, x] = colors[i+1]
            input[y+rect_height-1, x+rect_width-1] = colors[i+1]
        else:
            # make top right and bottom left corners colored in the input
            input[y, x+rect_width-1] = colors[i+1]
            input[y+rect_height-1, x] = colors[i+1]

    return input, output



def example_func():
    return generate_example