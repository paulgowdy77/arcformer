import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 5,

        'min_height': 6,
        'max_height': 10,
        'min_width': 6,
        'max_width': 10,

        'colors': random.sample(range(0,9), 6)
    }

    return config


def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    colors = config['colors']

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    for i in range(1,height-2):
        for j in range(1,width-2):

            if random.random() > 0.75:
                if input[i-1,j-1] == colors[0] and input[i-1,j] == colors[0] and input[i,j-1] == colors[0] \
                    and input[i-2,j-2] == colors[0] and input[i,j-2] == colors[0] and input[i-2,j] == colors[0] \
                        and input[i-1,j+1] == colors[0] and input[i-2,j-1] == colors[0] and input[i-1,j+2] == colors[0] \
                            and input[i-2,j+2] == colors[0] and input[i-1,j-2] == colors[0]:
                    

                                color_ind = random.randint(1,3)
                                center_color = colors[color_ind]
                                input[i,j] = center_color
                                output[i,j] = center_color

                                if color_ind == 1:
                                      output[i-1,j-1] = colors[4]
                                      output[i-1,j+1] = colors[4]
                                      output[i+1,j-1] = colors[4]
                                      output[i+1,j+1] = colors[4]
                                if color_ind == 2:
                                      output[i,j-1] = colors[5]
                                      output[i,j+1] = colors[5]
                                      output[i+1,j] = colors[5]
                                      output[i-1,j] = colors[5]
                                      


    return input, output



def example_func():
    return generate_example