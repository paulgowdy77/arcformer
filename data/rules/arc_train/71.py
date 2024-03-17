import numpy as np
import random

# ARC Public training set 71

# variant idea - instead of mirroring, just slide it over

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
    }

    return config




def generate_example(config):

    colors = random.sample(range(0, 9), 3)

    height = random.randint(14, 22)
    width = random.randint(14, 22)

    input = np.ones((height, width), dtype=int) * colors[0]
    output = np.ones((height, width), dtype=int) * colors[0]

    # generate stamp

    stamp_width = random.randint(4, 6)
    stamp_height = random.randint(4, 6)

    stamp = np.ones((stamp_height, 2*stamp_width), dtype=int) * colors[0]
    for i in range(stamp_height):
        for j in range(stamp_width):
            if random.random() < 0.75:
                stamp[i, j] = colors[1]
                # mirror stamp
                stamp[i, 2*stamp_width - j-1] = colors[1]

    # place stamp
    stamp_top = random.randint(0, height - stamp_height)
    stamp_left = random.randint(0, width - 2*stamp_width)

    input[stamp_top:stamp_top + stamp_height, stamp_left:stamp_left + 2*stamp_width] = stamp
    output[stamp_top:stamp_top + stamp_height, stamp_left:stamp_left + 2*stamp_width] = stamp

    # put a block over the stamp in the input
    block_width = random.randint(2, 4)
    block_height = random.randint(2, 4)
    block_top = random.randint(stamp_top-1, stamp_top + stamp_height - block_height)
    block_left = random.randint(stamp_left-1, stamp_left + stamp_width - block_width)

    input[block_top:block_top + block_height, block_left:block_left + block_width] = colors[2]


    




   



    return input, output



def example_func():
    return generate_example