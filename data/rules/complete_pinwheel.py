import numpy as np
import random

def generate_config():
    colors = random.sample(range(0, 9), 3)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 18,
        'max_height': 20,
        'min_width': 18,
        'max_width': 20,

        'colors': colors,
    }

    return config

def generate_stamp(colors):
    stamp_height = random.randint(4,6)
    stamp_width = 5
    stamp = np.ones((stamp_height, stamp_width)) * colors[0]
    stamp_out = np.ones((stamp_height, stamp_width)) * colors[0]

    stamp[:,2] = colors[1]
    stamp_out[:,2] = colors[2]

    for i in range(stamp_height-2):
        if random.random() > 0.35:
            stamp[i,1] = colors[1]
            stamp[i,3] = colors[1]
            stamp_out[i,1] = colors[2]
            stamp_out[i,3] = colors[2]

            if random.random() > 0.66:
                stamp[i,0] = colors[1]
                stamp[i,4] = colors[1]
                stamp_out[i,0] = colors[2]
                stamp_out[i,4] = colors[2]

    return stamp, stamp_out


def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    colors = config['colors']

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    center_y = random.randint(int(height/2)-2, int(height/2)+2)
    center_x = random.randint(int(width/2)-2, int(width/2)+2)

    stamp, stamp_out = generate_stamp(colors)

    input[center_y, center_x] = colors[1]
    output[center_y, center_x] = colors[1]
    

    input[center_y-stamp.shape[0]:center_y, center_x-2:center_x+3] = stamp

    output[center_y-stamp.shape[0]:center_y, center_x-2:center_x+3] = stamp 
    #print(stamp.shape)
    z = np.rot90(stamp, 1)
    #print(z.shape)
    input[center_y-2:center_y+3, center_x-stamp.shape[0]:center_x] = z
    output[center_y-2:center_y+3, center_x-stamp.shape[0]:center_x] = z
    z = np.rot90(stamp, 2)
    input[center_y+1:center_y+stamp.shape[0]+1,center_x-2:center_x+3] = z
    output[center_y+1:center_y+stamp.shape[0]+1,center_x-2:center_x+3] = z

    output[center_y-2:center_y+3, center_x+1:center_x+stamp.shape[0]+1] = np.rot90(stamp_out,3)

    if random.random() > 0.5:
        input = np.rot90(input, 1)
        output = np.rot90(output, 1)

    if random.random() > 0.5:
        input = np.rot90(input, 1)
        output = np.rot90(output, 1)

    # if random.random() > 0.5:
    #     input = np.rot90(input, 1)
    #     output = np.rot90(output, 1)

    if random.random() > 0.5:
        input = np.flip(input, 0)
        output = np.flip(output, 0)

    return input, output



def example_func():
    return generate_example