import numpy as np
import random

def generate_config():

    config = {
       
    }

    return config

def generate_stamp(bg_color, fg_color, stamp_size):
    stamp = np.ones((stamp_size, stamp_size)) * bg_color
    for i in range(stamp_size):
        for j in range(stamp_size):
            if random.random() > 0.25:
                stamp[i, j] = fg_color
    return stamp

def generate_example(config):

    height = random.randint(18, 24)
    width = random.randint(18, 24)

    colors = random.sample(range(0, 9), 3)
    input = np.ones((height, width)) * colors[0]
    output = input.copy()

    stamp_size = random.randint(2, 4)
    stamp_A = generate_stamp(colors[0], colors[1], stamp_size)
    stamp_B = generate_stamp(colors[0], colors[2], stamp_size)

    stamp_A_count = random.randint(1, 4)
    stamp_B_count = random.randint(1, 4)

    # generate all stamp locations together
    # avoid any overlap
    stamp_locations = []
    while len(stamp_locations) < stamp_A_count + stamp_B_count:
        x = random.randint(0, width-stamp_size-1)
        y = random.randint(0, height-stamp_size-1)
        # check if the stamp will overlap with any existing stamp
        # if it doesnt overlap, add it to the list
        # if it does, then try again
        overlap = False
        for loc in stamp_locations:
            if abs(loc[0]-x) < stamp_size and abs(loc[1]-y) < stamp_size:
                overlap = True
                break
        if not overlap:
            stamp_locations.append((x, y))
            

    for i in range(stamp_A_count):
        x, y = stamp_locations[i]
        input[y:y+stamp_size, x:x+stamp_size] = stamp_A
        output[y:y+stamp_size, x:x+stamp_size] = stamp_B
    
    for i in range(stamp_A_count, stamp_A_count+stamp_B_count):
        x, y = stamp_locations[i]
        input[y:y+stamp_size, x:x+stamp_size] = stamp_B
        output[y:y+stamp_size, x:x+stamp_size] = stamp_A

    

    return input, output



def example_func():
    return generate_example