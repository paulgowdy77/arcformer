import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 10,
        'max_height': 12,
        'min_width': 10,
        'max_width': 12,
    }

    return config

def generate_pattern(colors):
    pattern = np.ones((5,5)) * colors[0]
    in_pattern = np.ones((5,5)) * colors[0]
    #groups
    a = [(0,0), (0,4), (4,0), (4,4)]
    b = [(0,2), (2,0), (2,4), (4,2)]
    c = [(1,1), (1,3), (3,1), (3,3)]
    d = [(2,2)]

    groups = [a,b,c,d]

    #randomize
    for g in groups:
        c = random.randint(1,3)
        for p in g:
            pattern[p] = colors[c]
            in_pattern[p] = colors[c]
        # if len(g) > 1:
        #     d = random.choice([1,1,2,2,3])
        #     deletes = random.sample(g, d)
        #     for p in deletes:
        #         #pattern[p] = colors[0]
        #         in_pattern[p] = colors[0]

    color_deletes = random.choice([1,1,2,2,3])

    for i in range(color_deletes):
        g = groups[i]
        d = random.choice([1,1,2,2,3])
        deletes = random.sample(g, d)
        for p in deletes:
            #pattern[p] = colors[0]
            in_pattern[p] = colors[0]

    return pattern, in_pattern

    

def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    colors = random.sample(range(0, 9), 4)

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    x = random.randint(3, width-3)
    y = random.randint(3, height-3)


    output[y-2:y+3,x-2:x+3], input[y-2:y+3,x-2:x+3] = generate_pattern(colors)

    


    return input, output



def example_func():
    return generate_example