import numpy as np
import random

# ARC Public training set 117

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
    }

    return config




def generate_example(config):

    colors = random.sample(range(0, 9), 3)

    height = random.randint(14, 20)
    width = random.randint(14, 20)

    input = np.ones((height, width), dtype=int) * colors[0]
    output = np.ones((height, width), dtype=int) * colors[0]

    central_stamp = np.ones((3, 3), dtype=int) * colors[0]
    central_stamp[1, 1] = colors[1]
    central_stamp[0,0] = colors[1]
    central_stamp[0,2] = colors[1]
    central_stamp[2,0] = colors[1]
    central_stamp[2,2] = colors[1]

    radial_stamp = np.ones((4, 4), dtype=int) * colors[0]
    for i in range(4):
        for j in range(4):
            if random.random() < 0.65:
                radial_stamp[i, j] = colors[2]

    # central stamp center
    center_x = random.randint(6, width-6)
    center_y = random.randint(6, height-6)

    input[center_y-1:center_y+2, center_x-1:center_x+2] = central_stamp
    output[center_y-1:center_y+2, center_x-1:center_x+2] = central_stamp

    # place radial stamp in input
    input[center_y - 5:center_y - 1, center_x - 5:center_x - 1] = radial_stamp

    # rotate radial stamp and place 4x in output
    output[center_y - 5:center_y - 1, center_x - 5:center_x - 1] = radial_stamp
    output[center_y - 5:center_y - 1, center_x + 2:center_x + 6] = np.fliplr(radial_stamp)
    output[center_y + 2:center_y + 6, center_x - 5:center_x - 1] = np.flipud(radial_stamp)
    output[center_y + 2:center_y + 6, center_x + 2:center_x + 6] = np.flipud(np.fliplr(radial_stamp))


    # randomly flip and rotate input and output
    if random.random() < 0.5:
        input = np.flipud(input)
        output = np.flipud(output)
    if random.random() < 0.5:
        input = np.fliplr(input)
        output = np.fliplr(output)
    if random.random() < 0.75:
        x = random.randint(0, 6)
        input = np.rot90(input, x)
        output = np.rot90(output, x)
    

    



    return input, output



def example_func():
    return generate_example