import numpy as np
import random

# ARC Public training set 170

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
    }

    return config




def generate_example(config):

    colors = random.sample(range(0, 9), 7)
    bg_color = colors[0]
    # colors[1] is reserved for the oversized stamp


    
    input_size = 40

    while input_size > 30:
        output_size = random.randint(3, 5)
        output = np.ones((output_size, output_size), dtype=int) * bg_color

        # calculate the input size
        # needs to have room for the oversized stamp AND the output colormap
        # and plenty of margin

        oversized_stamp_cell_size = random.randint(3, 5)
        oversized_stamp_size = output_size * oversized_stamp_cell_size
        input_dim_min = oversized_stamp_size + output_size + 2
        input_dim_max = oversized_stamp_size + output_size + 6
        input_size = random.randint(input_dim_min, input_dim_max)

    input = np.ones((input_size, input_size), dtype=int) * bg_color

    # output colormap
    output_colormap = np.ones((output_size,output_size), dtype=int) * bg_color
    for i in range(output_size):
        for j in range(output_size):
            output_colormap[i,j] = random.choice(colors[2:])

    # place the output colormap in the input in the top output_size+2 rows
    # offset random or something


   



    return input, output



def example_func():
    return generate_example