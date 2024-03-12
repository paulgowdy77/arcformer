import numpy as np
import random

def generate_config():
    config = {
        'colors': random.sample(range(0, 9), 3),
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

    fixed_colors = config['colors']
    shape_color = random.sample(range(0, 9), 1)

    while shape_color in fixed_colors:
        shape_color = random.sample(range(0, 9), 1)

    shape_color = shape_color[0]

    width = random.randint(10,20)
    height = random.randint(10,20)

    input = np.ones((height, width)) * fixed_colors[0]
    output = input.copy()


    stamp_size = random.choice([2,3,3,4,4])
    stamp = generate_stamp(fixed_colors[0], shape_color, stamp_size)
    # mirror the stamp, randomly left-right or up-down
    # combine with original stamp to create doubled
    if random.random() > 0.5:
        new_stamp = np.fliplr(stamp)
    else:
        new_stamp = np.flipud(stamp)

    stamp = np.concatenate((stamp, new_stamp), axis=1)
    # randomly flip, rotate this stamp
    if random.random() > 0.5:
        stamp = np.rot90(stamp)
    # place the stamp randomly on the output and input
    stamp_x = random.randint(0, width - stamp_size*2)
    stamp_y = random.randint(0, height - stamp_size)
    input[stamp_y:stamp_y+stamp_size, stamp_x:stamp_x+stamp_size*2] = stamp
    output[stamp_y:stamp_y+stamp_size, stamp_x:stamp_x+stamp_size*2] = stamp

    # erase half the stamp on the input
    input[stamp_y:stamp_y+stamp_size, stamp_x:stamp_x+stamp_size] = fixed_colors[0]

    
    

    
    return input, output



def example_func():
    return generate_example