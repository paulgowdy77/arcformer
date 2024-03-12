import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 14,
        'max_height': 18,
        'min_width': 16,
        'max_width': 20,
    }

    return config


def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    nb_lines = random.randint(1,3)
    nb_extra_dot_colors = random.randint(1,2)
    colors = random.sample(range(0, 9), 1+nb_lines+nb_extra_dot_colors)

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    line_vert_coords = random.sample(range(0, int(height/3)), nb_lines)
    line_vert_coords = [x*3 for x in line_vert_coords]

    for i in range(nb_lines + nb_extra_dot_colors):
        nb_dots = random.randint(1,4)
        for j in range(nb_dots):
            dot_x = random.randint(0, width-1)
            dot_y = random.randint(0, height-1)
            while dot_y in line_vert_coords:
                dot_y = random.randint(0, height-1)
            input[dot_y, dot_x] = colors[i + 1]
            #output[dot_y, dot_x] = colors[i + 1]

            if i < nb_lines:
                if dot_y < line_vert_coords[i]:
                    output[line_vert_coords[i]-1, dot_x] = colors[i + 1]
                else:
                    output[line_vert_coords[i]+1, dot_x] = colors[i + 1]

    for i in range(nb_lines):
        input[line_vert_coords[i], :] = colors[i + 1]
        output[line_vert_coords[i], :] = colors[i + 1]

    if random.random() > 0.5:
        input = np.rot90(input, 1)
        output = np.rot90(output,1)

    return input, output



def example_func():
    return generate_example