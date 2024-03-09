import numpy as np
import random

def generate_config():
    config = {
        'copy_number': random.randint(2, 4),
        'stamp_size': random.randint(3, 5),
        'rotate': random.choice([True, False]),
    }
    return config


def generate_stamp(bg_color, fg_color, size):
    stamp = np.ones((size, size)) * bg_color
    for i in range(size):
        for j in range(size):
            if random.random() < 0.75:
                stamp[i, j] = fg_color
    return stamp


def generate_example(config):
    colors = random.sample(range(0, 9), 2)

    input_width = random.randint(14, 20)
    input_height = random.randint(14, 20)
    input = np.ones((input_height, input_width)) * colors[0]

    # generate stamp
    stamp_size = config['stamp_size']
    stamp = generate_stamp(colors[0], colors[1], stamp_size)

    # place stamp randomly on input
    stamp_x = random.randint(0, input_width - stamp_size)
    stamp_y = random.randint(0, input_height - stamp_size)
    input[stamp_y:stamp_y+stamp_size, stamp_x:stamp_x+stamp_size] = stamp

    # copy stamp
    copy_number = config['copy_number']
    output = np.ones((stamp_size, stamp_size*copy_number)) * colors[0]
    for i in range(copy_number):
        output[:, i*stamp_size:(i+1)*stamp_size] = stamp

    if config['rotate']:
        output = np.rot90(output)

    return input, output



def example_func():
    return generate_example