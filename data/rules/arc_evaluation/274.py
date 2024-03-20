import numpy as np
import random

# ARC Public eval set 274
# sliding colored tiles

# Issues: theres only one set of squares, they all go in the same direction, and the color palette is always in the top right

def generate_config():

    config = {
    }

    return config


def generate_example(config):

    nb_colors = random.randint(2, 5)
    colors = random.sample(range(0, 9), nb_colors+2)
    tile_colors = colors[2:]

    height = random.randint(16, 22)
    width = random.randint(16, 22)

    nb_squares = random.randint(5, 10)
    direction = random.choice(['left', 'right'])

    square_size = random.randint(3,4)

    square_start_x = random.randint(1, width - nb_squares - square_size)
    square_start_y = random.randint(1, height - nb_squares - square_size)

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]  

    for i in range(nb_squares):
        input[square_start_y+i:square_start_y+square_size+i,square_start_x+i:square_start_x+square_size+i] = colors[1]
        output[square_start_y+i:square_start_y+square_size+i,square_start_x+i:square_start_x+square_size+i] = tile_colors[i%nb_colors]
  
    for i in range(nb_colors):
        input[0,i] = colors[i+2]

    return input, output



def example_func():
    return generate_example