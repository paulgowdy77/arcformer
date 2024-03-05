import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 16,
        'max_height': 20,
        'min_width': 16,
        'max_width': 20,
    }

    return config

def generate_stamp(colors, width, height):
    stamp1 = np.ones((height, width)) * colors[0]
    stamp2 = np.ones((height,width)) * colors[0]

    for i in range(height):
        for j in range(width):
            if random.random() < 0.45:
                stamp1[i,j] = colors[1] 

    for i in range(3):
        x = random.randint(0,height-1)
        y = random.randint(0,width-1)

        stamp1[x,y]= colors[2+i]
        stamp2[x,y]= colors[2+i]

    return stamp1, stamp2


def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    colors = random.sample(range(0, 9), 5)

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    stamp_width = random.randint(3,5)
    stamp_height = random.randint(3,5)

    stamp_full, stamp_empty = generate_stamp(colors, stamp_width, stamp_height)

    nb_rotations = random.randint(0,3)
    nb_flips = random.randint(0,1)

    #print(stamp_empty.shape)

    stamp_empty = np.rot90(stamp_empty, nb_rotations)
    stamp_empty = np.flip(stamp_empty, nb_flips)

    #print(stamp_empty.shape)
    x = random.randint(0, width - stamp_width-1)
    y = random.randint(0, height - stamp_height-1)

    input[y:y+stamp_height, x:x+stamp_width] = stamp_full

    empty_x = random.randint(0, width - stamp_width-1)
    empty_y = random.randint(0, height - stamp_height-1)

    #make sure stamps dont overlap
    while empty_x +stamp_width > x and empty_x < x+stamp_width and empty_y + stamp_height > y and empty_y < y+stamp_height:
        empty_x = random.randint(0, width - stamp_width-1)
        empty_y = random.randint(0, height - stamp_height-1)

    try:
        input[empty_y:empty_y+stamp_height, empty_x:empty_x+stamp_width] = stamp_empty
    except:
        input[empty_y:empty_y+stamp_width, empty_x:empty_x+stamp_height] = stamp_empty

    stamp_full = np.rot90(stamp_full, nb_rotations)
    stamp_full = np.flip(stamp_full, nb_flips)
    
    try:
        output[empty_y:empty_y+stamp_height, empty_x:empty_x+stamp_width] = stamp_full
    except:
        output[empty_y:empty_y+stamp_width, empty_x:empty_x+stamp_height] = stamp_full

    









    


    return input, output



def example_func():
    return generate_example