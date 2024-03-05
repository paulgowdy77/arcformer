import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

        # 'min_height': 6,
        # 'max_height': 12,
        # 'min_width': 6,
        # 'max_width': 12,
    }

    return config

def generate_stamp(colors):
    s = np.ones((3,3)) * colors[0]
    for i in range(3):
        for j in range(3):
            if random.random() > 0.2:
                s[i,j] = colors[1]
    return s


def generate_example(config):
    

    colors = random.sample(range(0, 9), 2)

    z = np.ones((9,9)) * colors[0]
    output = np.ones((9, 9)) * colors[0]

    stamp = generate_stamp(colors)

    for i in range(3):
        for j in range(3):
            if stamp[i,j] == colors[1]:
                output[i*3:(i+1)*3,j*3:(j+1)*3] = stamp
                z[i*3:(i+1)*3,j*3:(j+1)*3] = colors[1]

    
    input = np.ones((random.randint(12,18),random.randint(12,18))) * colors[0]
    top_left = (random.randint(1, input.shape[0]-10), random.randint(1, input.shape[1]-10))
    input[top_left[0]:top_left[0]+9, top_left[1]:top_left[1]+9] = z
  

    return input, output



def example_func():
    return generate_example