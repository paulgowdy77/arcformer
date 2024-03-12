import numpy as np
import random

def generate_config():
    config = {
        "corner_fill_color": random.choice([0,1,2,3,4,5,6,7,8,9]),
    }
    return config



def generate_example(config):

    corner_fill_color = config["corner_fill_color"]

    colors = random.sample([0,1,2,3,4,5,6,7,8,9], 2)
    # make sure the colors are different
    while corner_fill_color in colors:
        colors = random.sample([0,1,2,3,4,5,6,7,8,9], 2)

    #print(colors, corner_fill_color)

    height = random.randint(12, 18)
    width = random.randint(12, 18)

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    number_of_squares = random.choice([1,2,3,4])

    # place non-overlapping squares in the input
    for _ in range(number_of_squares):
        x = random.randint(0, width-2)
        y = random.randint(0, height-2)

        # check for overlap
        while any(input[y:y+2, x:x+2].flatten() != colors[0]):
            x = random.randint(0, width-2)
            y = random.randint(0, height-2)

        input[y:y+2, x:x+2] = colors[1]
        output[y:y+2, x:x+2] = colors[1]

        # delete one random square in the square
        x1 = random.randint(x, x+1)
        y1 = random.randint(y, y+1)
        input[y1, x1] = colors[0]
        output[y1, x1] = corner_fill_color

    input, output = output, input

    return input, output

def example_func():
    return generate_example