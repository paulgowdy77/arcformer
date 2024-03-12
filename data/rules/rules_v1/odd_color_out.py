import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,
        'colors': random.sample(range(0, 9), 7),

    }

    return config

def generate_multicolor_stamp(bg_color, colors):
    stamp = np.ones((3,3)) * bg_color
    nb_colors = len(colors)
    random.shuffle(colors)
    positions = random.sample(range(0, 8), nb_colors)

    for i, p in enumerate(positions):
        stamp[p//3, p%3] = colors[i]

    return stamp




def generate_example(config):


    colors = config['colors']

    input = np.ones((11, 11)) * colors[0]
    output = np.ones((1, 1)) * colors[6]

   
    for i in range(11):
        input[i, 3] = colors[1]
        input[i, 7] = colors[1]
        #output[i, 3] = colors[1]
        #output[i, 7] = colors[1]
    for i in range(11):
        input[3,i] = colors[1]
        input[7,i] = colors[1]
        #output[3,i] = colors[1]
        #output[7,i] = colors[1]

    four_color = random.randint(0,8)

    for i in range(3):
        for j in range(3):
            if (i*3) + j == four_color:
                stamp = generate_multicolor_stamp(colors[0], colors[2:6])
                #output = process_output(output, stamp)
            else:
                stamp = generate_multicolor_stamp(colors[0], colors[2:7])

            input[i*3 + i:i*3+3 + i, j*3 + j:j*3+3 + j] = stamp

    return input, output



def example_func():
    return generate_example