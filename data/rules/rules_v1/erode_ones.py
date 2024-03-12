import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 14,
        'max_height': 18,
        'min_width': 14,
        'max_width': 18,
    }

    return config

def not_overlapping(x, y, h, w, shapes):
    for s in shapes:
        if not (x+w < s[1] or x > s[1]+s[3] or y+h < s[0] or y > s[0]+s[2]):
            return False
    return True


def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    colors = random.sample(range(0, 9), 2)

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    nb_shapes = random.randint(1, 3)

    shapes = []

    while len(shapes) < nb_shapes:
        h=random.randint(3,5)
        w = random.randint(3,5)
        x = random.randint(1, width - w-1)
        y = random.randint(1, height - h-1)


        if not_overlapping(x, y, h, w, shapes):
            shapes.append((y,x,h,w))

    
    for s in shapes:
        input[s[0]:s[0]+s[2], s[1]:s[1]+s[3]] = colors[1]
        output[s[0]:s[0]+s[2], s[1]:s[1]+s[3]] = colors[1]
            

    for i in range(height):
        for j in range(width):
            if random.random() > 0.95:
                input[i,j] = colors[1]



    return input, output



def example_func():
    return generate_example