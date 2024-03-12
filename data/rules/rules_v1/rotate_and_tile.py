import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,
        'dir': random.choice([-1,1])
    }

    return config

def generate_stamp(colors):
    s = np.ones((3,3)) * colors[0]
    for i in range(3):
        for j in range(3):
            z = random.randint(1,len(colors)-1)
            s[i,j] = colors[z]
    return s

def generate_example(config):
    

    colors = random.sample(range(0, 9), 6)

    input = np.ones((3, 3)) * colors[0]
    output = np.ones((6, 6)) * colors[0]

    
    stamp = generate_stamp(colors)
    input = np.copy(stamp)

    output[0:3,0:3] = stamp
    output[0:3,3:6] = np.rot90(stamp,1*config['dir'])
    output[3:6,0:3] = np.rot90(stamp,3*config['dir'])
    output[3:6,3:6] = np.rot90(stamp,2*config['dir'])

    return input, output



def example_func():
    return generate_example