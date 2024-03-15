import numpy as np
import random

# ARC Public training set 33

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        "fixed_color": random.randint(0, 9)
    }

    return config

def generate_stamp(bg_color, color_1, color_2):
    stamp = np.ones((3,3))*bg_color
    new_stamp = np.ones((3,3))*bg_color
    for i in range(3):
        for j in range(3):
            if random.random() < 0.75:
                stamp[i, j] = color_1
                new_stamp[i, j] = color_2
    return stamp, new_stamp


def generate_example(config):

    colors = random.sample(range(0, 9), 3)

    input = np.ones((17, 17), dtype=int) * colors[0]
    output = np.ones((17, 17), dtype=int) * colors[0]

    # create grid lines
    input[:,5] = colors[1]
    input[5,:] = colors[1]
    output[:,5] = colors[1]
    output[5,:] = colors[1]

    input[:,11] = colors[1]
    input[11,:] = colors[1]
    output[:,11] = colors[1]
    output[11,:] = colors[1]

    top_left_stamp, new_stamp = generate_stamp(colors[0], colors[2], colors[1])

    input[1:4, 1:4] = top_left_stamp
    output[1:4, 1:4] = top_left_stamp

    # for the rest of the grid cells, place the new_stamp
    for i in [1, 7, 13]:
        for j in [1, 7, 13]:
            if i == 1 and j == 1:
                continue
            #input[i:i+3, j:j+3] = new_stamp
            output[i:i+3, j:j+3] = new_stamp

            for k in range(3):
                for l in range(3):
                    if output[i+k, j+l] == colors[0]:
                        continue
                    if random.random() < 0.5:

                        input[i+k, j+l] = colors[2]
                        output[i+k, j+l] = colors[2]
    

    



    return input, output



def example_func():
    return generate_example