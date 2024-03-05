import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 5,

        'min_height': 12,
        'max_height': 16,
        'min_width': 12,
        'max_width': 16,

        
    }

    return config

def generate_stamp(bg_color, stamp_color):
    s = np.ones((3,3)) * bg_color

    for i in range(3):
        for j in range(3):
                if random.random() > 0.3:
                    s[i,j] = stamp_color
    return s

def recolor_stamp(stamp, bg_color, new_color):
    for i in range(3):
        for j in range(3):
                if stamp[i,j] != bg_color:
                     stamp[i,j] = new_color
    
    return stamp



def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    colors = random.sample(range(0,9), 4)

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    stamp = generate_stamp(colors[0], colors[1])
    input[:3,:3] = stamp
    output[:3,:3] = stamp

    for i in range(3,height-3):
         for j in range(3,width-3):
              
            if random.random() > 0.95:
                if input[i-1,j-1] == colors[0] and input[i-1,j] == colors[0] and input[i,j-1] == colors[0] \
                    and input[i-2,j-2] == colors[0] and input[i,j-2] == colors[0] and input[i-2,j] == colors[0] \
                        and input[i-1,j+1] == colors[0] and input[i-2,j-1] == colors[0] and input[i-1,j+2] == colors[0] \
                            and input[i-2,j+2] == colors[0] and input[i-1,j-2] == colors[0]:
                                
                                c = random.randint(2,3)
                                input[i,j] = colors[c]

                                output[i-1:i+2,j-1:j+2] = recolor_stamp(stamp, colors[0], colors[c])

    
                                      


    return input, output



def example_func():
    return generate_example