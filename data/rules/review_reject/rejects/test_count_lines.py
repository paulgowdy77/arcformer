import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': random.randint(4,5),

        'min_height': 10,
        'max_height': 16,
        'min_width': 10,
        'max_width': 16,

        'colors': random.sample(range(0,9), 3),

        'rotate': random.randint(0,3)
    }

    return config


def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    colors = config['colors']

    bg_color = colors[0]

    while bg_color in colors:
        bg_color = random.randint(0, 9)

    input = np.ones((height, width)) * bg_color
    output = np.ones((2, 3)) * colors[0]

    nb_lines = random.randint(2, 6)

    c_count = 0

    for i in range(nb_lines):
        # generate horizontal line
        # dont overlap with any existing lines

        line_vert = random.randint(0, height - 1)
        line_horiz = random.randint(0, width - 1)

        line_length = random.randint(2, 7)

        while input[line_vert, line_horiz] != bg_color or line_horiz + line_length > width or input[line_vert, line_horiz + line_length - 1] != bg_color:
            line_vert = random.randint(0, height - 1)
            line_horiz = random.randint(0, width - 1)

        c = random.randint(0, 1)
        
        input[line_vert, line_horiz:line_horiz+line_length] = colors[1+c]
        c_count += c

    for i in range(nb_lines):
        if i < c_count:
            output[i // 3, i % 3] = colors[2]
        else:
            output[i // 3, i % 3] = colors[1]

    if config['rotate'] > 0:
        input = np.rot90(input, config['rotate'])
        output = np.rot90(output, config['rotate'])


    return input, output



def example_func():
    return generate_example