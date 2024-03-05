import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': random.randint(4,5),

        'min_height': 14,
        'max_height': 20,
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

    colors = random.sample(range(0, 9), 2)

    input = np.ones((height, width)) * colors[0]
    

    rows = random.randint(2,4)
    cols = random.randint(2,4)

    output = np.ones((rows+1, cols+1)) * colors[0]

    row_indices = [0]

    for i in range(rows):
        row_indices.append(row_indices[-1] + 1 + random.randint(1, 4))

    if row_indices[-1] > height - 2:
        row_indices[-1] = height - 2

    col_indices = [0]

    for i in range(cols):
        col_indices.append(col_indices[-1] + 1 + random.randint(1, 4))

    if col_indices[-1] > width - 2:
        col_indices[-1] = width - 2

    #print(rows, cols)

    for ri in row_indices[1:]:
        if ri < height - 1:
            input[ri, :] = colors[1]
        #input[ri, :] = colors[1]
    for ci in col_indices[1:]:
        if ci < width -1:
            input[:, ci] = colors[1]



    return input, output



def example_func():
    return generate_example