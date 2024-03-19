import numpy as np
import random

# ARC Public training set 88

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
    }

    return config




def generate_example(config):

    colors = random.sample(range(0, 9), 3)

    stamp_width = random.randint(3, 8)
    stamp_height = random.randint(3, 8)

    stamp = np.ones((stamp_height, stamp_width), dtype=int) * colors[0]
    other_stamp = np.ones((stamp_height, stamp_width), dtype=int) * colors[0]

    for i in range(stamp_height):
        for j in range(stamp_width):
            if random.random() < 0.65:
                stamp[i, j] = colors[2]
                other_stamp[i, j] = colors[1]

    bigger_stamp = np.ones((stamp_height+2, stamp_width+2), dtype=int) * colors[0]
    bigger_stamp[1:stamp_height+1, 1:stamp_width+1] = other_stamp
    bigger_stamp[0, 0] = colors[2]
    bigger_stamp[0, -1] = colors[2]
    bigger_stamp[-1, 0] = colors[2]
    bigger_stamp[-1, -1] = colors[2]

    output = stamp
    input_height = random.randint(12, 18)
    input_width = random.randint(12, 18)

    input = np.ones((input_height, input_width), dtype=int) * colors[0]
    # place bigger stamp in input
    bigger_stamp_x = random.randint(0, input_width-stamp_width-2)
    bigger_stamp_y = random.randint(0, input_height-stamp_height-2)
    input[bigger_stamp_y:bigger_stamp_y+stamp_height+2, bigger_stamp_x:bigger_stamp_x+stamp_width+2] = bigger_stamp

    



    return input, output



def example_func():
    return generate_example