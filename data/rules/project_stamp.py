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

def generate_stamp(bg_color, shape_color):
    stamp = np.ones((3,3)) * bg_color
    for i in range(3):
        for j in range(3):
            if random.random() > 0.25:
                stamp[i,j] = shape_color
    return stamp

DIR_DICT = {
    0:{
        'center': [-4,-4],
        'capture': np.array([[0,0,0],[0,0,1],[0,1,1]])
    },
    1:{
        'center': [-4,0],
        'capture': np.array([[0,0,0],[0,0,0],[1,1,1]])
    },
    2:{
        'center': [-4,4],
        'capture': np.array([[0,0,0],[1,0,0],[1,1,0]])
    },
    3:{
        'center': [0,-4],
        'capture': np.array([[0,0,1],[0,0,1],[0,0,1]])
    },
    4:{
        'center': [0,4],
        'capture': np.array([[1,0,0],[1,0,0],[1,0,0]])
    },
    5:{
        'center': [4,-4],
        'capture': np.array([[0,1,1],[0,0,1],[0,0,0]])
    },
    6:{
        'center': [4,0],
        'capture': np.array([[1,1,1],[0,0,0],[0,0,1]])
    },
    7:{
        'center': [4,4],
        'capture': np.array([[1,1,0],[1,0,0],[0,0,0]])
    },
}


def pad(i):
    p = np.zeros((i.shape[0]+10, i.shape[1]+10))
    p[5:-5, 5:-5] = i
    return p

def unpad(i):
    return i[5:-5, 5:-5]


def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    nb_directions = random.choice([1,2,2])
    directions = random.sample(range(0,8), nb_directions)

    colors = random.sample(range(0, 9), nb_directions + 2)

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    midpoint = (random.randint(4, height-4), random.randint(4, width-4))
    stamp = generate_stamp(colors[0], colors[1])

    input[midpoint[0] - 1:midpoint[0]+2, midpoint[1]-1:midpoint[1]+2] = stamp
    output[midpoint[0] - 1:midpoint[0]+2, midpoint[1]-1:midpoint[1]+2] = stamp

    input = pad(input)
    output = pad(output)
    midpoint = (midpoint[0]+5, midpoint[1]+5)

    for i, d in enumerate(directions):
        center = DIR_DICT[d]['center']
        capture = DIR_DICT[d]['capture']

        z = np.zeros((3, 3))
        x = np.zeros((3, 3))
        for j in range(3):
            for k in range(3):
                if stamp[j,k] == colors[1]:
                    x[j,k] = colors[i+2]
                else:
                    x[j,k] = colors[0]
                if capture[j,k] == 1 and stamp[j,k] == colors[1]:
                    z[j,k] = colors[i+2]
                else:
                    z[j,k] = colors[0]


        
        
        input[midpoint[0] + center[0] - 1:midpoint[0] + center[0] + 2, midpoint[1] + center[1] - 1:midpoint[1] + center[1] + 2] = z
    
        output[midpoint[0] + center[0] - 1:midpoint[0] + center[0] + 2, midpoint[1] + center[1] - 1:midpoint[1] + center[1] + 2] = x


    input = unpad(input)
    output = unpad(output)
    return input, output



def example_func():
    return generate_example