import numpy as np
import random

# ARC Public training set 179

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
    }

    return config



def generate_example(config):

    colors = random.sample(range(0, 9), 7)

    input = np.ones((9, 9), dtype=int) * colors[0]
    output = np.ones((6, 6), dtype=int) * colors[0]

    input[:,2] = colors[1]
    input[2,:] = colors[1]

    last_four_colors = colors[3:]

    for i in range(6):
        for j in range(6):
            if random.random() < 0.65:
                input[3+i, 3+j] = colors[2]
                if i < 3 and j < 3:
                    output[i, j] = last_four_colors[0]
                elif i < 3 and j >= 3:
                    output[i, j] = last_four_colors[1]
                elif i >= 3 and j < 3:
                    output[i, j] = last_four_colors[2]
                else:
                    output[i, j] = last_four_colors[3]

    input[0,0] = colors[3]
    input[0,1] = colors[4]
    input[1,0] = colors[5]
    input[1,1] = colors[6]

    # randomly flip the input and output
    if random.random() < 0.5:
        input = np.flip(input, 0)
        output = np.flip(output, 0)
    if random.random() < 0.5:
        input = np.fliplr(input)
        output = np.fliplr(output)
    if random.random() < 0.5:
        input = np.flipud(input)
        output = np.flipud(output)
    if random.random() < 0.5:
        x = random.randint(0, 3)
        input = np.rot90(input, x)
        output = np.rot90(output, x)
                
   
    



    return input, output



def example_func():
    return generate_example