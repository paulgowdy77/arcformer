import numpy as np
import random

def generate_config():

    num_rotations = random.randint(1,10)

    config = {
        'width': random.choice([3, 4, 5, 6]),
        'height': random.choice([3, 4, 5, 6]),
        
        
        'flips': [random.choice(['UD', 'LR']) for x in range(num_rotations)],

    }

    return config


def generate_example(config):

    nb_colors = random.randint(4, 6)
    colors = random.sample([0,1,2,3,4,5,6,7,8,9], nb_colors)
    input = np.ones((config['height'], config['width']), dtype=int) * colors[0]
    # = np.ones((config['height'], config['width']), dtype=int) * colors[0]

    # make a random pattern
    for i in range(config['height']):
        for j in range(config['width']):
            if random.random() < 0.5:
                input[i, j] = random.choice(colors[1:])

    output = np.copy(input)

    # apply flips
    for flip in config['flips']:
        if flip == 'UD':
            output = np.flipud(output)
        elif flip == 'LR':
            output = np.fliplr(output)



    return input, output



def example_func():
    return generate_example