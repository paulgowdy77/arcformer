import numpy as np
import random

def generate_config():
    colors = random.sample(range(0, 9), 4)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 14,
        'max_height': 18,
        'min_width': 14,
        'max_width': 18,

        'colors': colors,
    }

    return config

def generate_stamp(colors):
    stamp_height = random.randint(1, 3)
    stamp_width = random.randint(2,3)

    stamp1 = np.ones((stamp_height, stamp_width)) * colors[0]
    stamp2 = np.ones((stamp_height, stamp_width)) * colors[0]
    stamp3 = np.ones((stamp_height, stamp_width)) * colors[0]

    for i in range(stamp_height):
        for j in range(stamp_width):
            if random.random() > 0.5:
                stamp1[i,j] = colors[1]
                stamp2[i,j] = colors[2]
                stamp3[i,j] = colors[3]

    return stamp1, stamp2, stamp3


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

    stamp1, stamp2, stamp3 = generate_stamp(colors)
    stamps = [stamp1, stamp2, stamp3]
    
    end_vertical = random.randint(int(height/2) - 3, int(height/2) + 3)

    vert_offsets = [0] + random.sample(range(-5,5), 2)

    horizontal_positions = [2, random.randint(2,4)+stamp1.shape[1], random.randint(4,5)+stamp1.shape[1]*2]
    random.shuffle(horizontal_positions)
    for i in range(3):
        #print(stamps[i].shape)
        input[end_vertical+vert_offsets[i]:end_vertical+vert_offsets[i]+stamp1.shape[0], horizontal_positions[i]:horizontal_positions[i]+stamp1.shape[1]] = stamps[i]
        output[end_vertical:end_vertical+stamp1.shape[0], horizontal_positions[i]:horizontal_positions[i]+stamp1.shape[1]] = stamps[i]


    return input, output



def example_func():
    return generate_example