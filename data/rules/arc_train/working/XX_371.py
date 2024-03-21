import numpy as np
import random

# ARC Public training set 371
# ISSUE: even/odd distance weirdness
# ISSUE: fixed stamp, want to vary this

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        "fixed_color": random.randint(0, 9)
    }

    return config

def generate_stamp(bg_color, fg_color):
    stamp = np.ones((3,3))*bg_color
    for i in range(3):
        for j in range(3):
            if i == j:
                stamp[i, j] = fg_color
            if i == -j:
                stamp[i, j] = fg_color
    return stamp


def generate_example(config):

    fixed_color = config["fixed_color"]
    # sample two colors not in fixed color
    colors = random.sample([i for i in range(10) if i != fixed_color], 2)

    height = random.randint(14, 20)
    width = random.randint(14, 20)

    input = np.ones((height, width), dtype=int) * colors[0]
    output = np.ones((height, width), dtype=int) * colors[0]

    # place two dots in the input an odd distance apart
    min_dim = min(height, width)
    distance = random.choice(range(5, min_dim))
    if distance % 2 == 0:
        distance -= 1

    margin = min_dim - distance

    x1 = random.choice(range(2, margin))
    y1 = random.choice(range(2, margin))

    x2 = x1 + distance

    input[y1, x1] = colors[1]
    input[y1, x2] = colors[1]
    output[y1, x1] = colors[1]
    output[y1, x2] = colors[1]

    stamp = generate_stamp(colors[0], fixed_color)
    # place stamp halfway between the two dots in the output
    stamp_height, stamp_width = stamp.shape

    stamp_center_x = x1 + (distance // 2) + 1
    
    stamp_x = stamp_center_x - 1
    stamp_y = y1 - 1

    print(x1, distance, x2, stamp_x)

    output[stamp_y:stamp_y+stamp_height, stamp_x:stamp_x+stamp_width] = stamp
    
   


    return input, output



def example_func():
    return generate_example