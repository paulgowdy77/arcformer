import numpy as np
import random

# ARC Public training set 359
# denoise colored bars

def generate_config():

    config = {}

    return config


def generate_example(config):

    colors = list(range(10))
    random.shuffle(colors)
    nb_color_bars = random.randint(2, 5)

    height = random.randint(8,16)
    width = random.randint(16,22)

    input = np.ones((height, width)) * colors[0]

    total_length = 0
    for i in range(nb_color_bars):
        color = colors[i]
        bar_x = random.randint(3,6)

        input[:, total_length: total_length + bar_x] = color

        total_length += bar_x

    output = input.copy()
    
    # apply noise to the input
    for i in range(height):
        for j in range(width):
            if random.random() < 0.15:
                input[i,j] = random.choice(colors)

    
    #if random.random() > 0.5:
    n_rots = random.randint(0,3)
    input = np.rot90(input, k=n_rots)
    output = np.rot90(output, k=n_rots)
    




    return input, output



def example_func():
    return generate_example