import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {

    }

    return config


def generate_example(config):
 
    colors = random.sample(range(0, 9), 3)

    height = random.randint(16, 26)
    width = random.randint(16, 26)

    input = np.ones((height, width)) * colors[0]

    # create rectangle
    rect_height = random.randint(4, 10)
    rect_width = random.randint(6, 8)

    rect = np.ones((rect_height, rect_width)) * colors[1]

    for i in range(rect_height):
        for j in range(rect_width):
            if random.random() > 0.75:
                rect[i,j] = colors[2]

    output = rect.copy()

    # flip the rectangle left right
    rect = np.fliplr(rect)

    # place the rect in the input
    r = random.randint(0, height - rect_height)
    c = random.randint(0, width - rect_width)

    input[r:r+rect_height, c:c+rect_width] = rect

    


    return input, output



def example_func():
    return generate_example