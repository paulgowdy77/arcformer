import numpy as np
import random

# ARC Public eval set 109
# invert and tile

def generate_config():

    config = {
    }

    return config

def generate_stamp(stamp_size, bg_color, fg_color):
    stamp = np.ones((stamp_size, stamp_size)) * bg_color
    flipped_stamp = np.ones((stamp_size, stamp_size)) * fg_color
    for i in range(stamp_size):
        for j in range(stamp_size):
            if random.random() > 0.5:
                stamp[i,j] = fg_color
                flipped_stamp[i,j] = bg_color

    return stamp, flipped_stamp


def generate_example(config):

    colors = random.sample(range(0, 9), 2)
    stamp_size = random.randint(2, 4)

    stamp, flipped_stamp = generate_stamp(stamp_size, colors[0], colors[1])

    input = stamp

    output = np.zeros((stamp_size*2, stamp_size*2))
    for i in range(2):
        for j in range(2):
            output[i*stamp_size:(i+1)*stamp_size,j*stamp_size:(j+1)*stamp_size] = flipped_stamp
                           

    return input, output



def example_func():
    return generate_example