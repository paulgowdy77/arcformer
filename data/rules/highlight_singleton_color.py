import numpy as np
import random

def generate_config():

    config = {
        'fixed_colors': random.sample(range(0,9), 2)
    }

    return config


def generate_example(config):

    fixed_colors = config['fixed_colors']
    # get 5 more colors that are not in fixed_colors
    remaining_colors = list(set(range(0,9)) - set(fixed_colors))
    random.shuffle(remaining_colors)
    dot_colors = remaining_colors[:5]

    height = random.randint(12, 20)
    width = random.randint(12, 20)

    input = np.ones((height, width)) * fixed_colors[0]
    output = input.copy()

    for color in dot_colors[:-1]:
        dot_count = random.randint(2, 10)
        for j in range(dot_count):
            x = random.randint(0, width-1)
            y = random.randint(0, height-1)
            while input[y, x] != fixed_colors[0]:
                x = random.randint(0, width-1)
                y = random.randint(0, height-1)
            input[y, x] = color
    
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    while input[y, x] != fixed_colors[0]:
        x = random.randint(0, width-1)
        y = random.randint(0, height-1)
    input[y, x] = dot_colors[-1]
    output[y, x] = dot_colors[-1]

    # draw a border around the output dot
    output[y-1:y+2, x-1:x+2] = fixed_colors[1]
    output[y, x] = dot_colors[-1]


  


    return input, output



def example_func():
    return generate_example