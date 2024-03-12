import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    fixed_colors = random.sample(range(0, 9), 3)

    config = {
        'fixed_colors': fixed_colors,
    }

    return config


def generate_example(config):

    fixed_colors = config['fixed_colors']
    # generate two colors not in fixed_colors
    colors = random.sample([x for x in range(0,9) if x not in fixed_colors], 2)

    height = random.randint(12, 22)
    width = random.randint(12, 22)

    input = np.ones((height, width)) * fixed_colors[0]
    output = np.ones((height, width)) * fixed_colors[0]

    # draw a rectangle of colors[0] in the input and output
    rect_height = random.randint(4, 8)
    rect_width = random.randint(4, 8)

    rect_r = random.randint(0, height - rect_height)
    rect_c = random.randint(0, width - rect_width)

    for r in range(rect_r, rect_r + rect_height):
        for c in range(rect_c, rect_c + rect_width):
            input[r,c] = colors[0]
            output[r,c] = colors[0]

    # add random dots of colors[1] to both input and output
    for r in range(height):
        for c in range(width):
            if random.random() > 0.65:
                input[r,c] = colors[1]

                # if the dot is inside the rectangle, change it to fixed_colors[1]
                if r >= rect_r and r < rect_r + rect_height and c >= rect_c and c < rect_c + rect_width:
                    output[r,c] = fixed_colors[1]
                else:
                    output[r,c] = colors[1]

   


    return input, output



def example_func():
    return generate_example