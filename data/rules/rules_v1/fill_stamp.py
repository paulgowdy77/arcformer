import numpy as np
import random

def generate_config():

    num_rotations = random.randint(1,10)

    config = {
        'colors': random.sample([0,1,2,3,4,5,6,7,8,9], 3),

    }

    return config

def make_3x3_stamp_pair(bg_color, color, fill_color):
    empty_stamp = np.ones((3,3), dtype=int) * bg_color
    fill_stamp = np.ones((3,3), dtype=int) * bg_color

    for i in range(3):
        for j in range(3):
            if random.random() < 0.75:
                empty_stamp[i, j] = color
                fill_stamp[i, j] = color
            else:
                fill_stamp[i, j] = fill_color
            
    return empty_stamp, fill_stamp


def generate_example(config):

    height = random.choice([12,13, 14, 15, 16,17,18])
    width = random.choice([12,13, 14, 15, 16,17,18])
    colors = config['colors']
    input = np.ones((height, width), dtype=int) * colors[0]
    output = np.ones((height, width), dtype=int) * colors[0]

    # make 2 or 3 random 3x3 stamps
    nb_stamps = random.choice([2,3])

    # make the stamp positions non-overlapping
    stamp_xs = []
    stamp_ys = []
    for i in range(nb_stamps):
        x = random.randint(0, width-3)
        y = random.randint(0, height-3)
        # check if the stamp overlaps with any other stamp
        while any([abs(x - sx) < 3 and abs(y - sy) < 3 for sx, sy in zip(stamp_xs, stamp_ys)]):
            x = random.randint(0, width-3)
            y = random.randint(0, height-3)
        stamp_xs.append(x)
        stamp_ys.append(y)
    
    for i in range(nb_stamps):
        stamp_x = stamp_xs[i]
        stamp_y = stamp_ys[i]

        empty_stamp, fill_stamp = make_3x3_stamp_pair(colors[0], colors[1], colors[2])
        input[stamp_y:stamp_y+3, stamp_x:stamp_x+3] = empty_stamp
        output[stamp_y:stamp_y+3, stamp_x:stamp_x+3] = fill_stamp

    return input, output



def example_func():
    return generate_example