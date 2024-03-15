import numpy as np
import random

# ARC Public training set 368

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        "fixed_colors": random.sample(range(0, 9), 5)
    }

    return config


def generate_example(config):

    fixed_colors = config['fixed_colors']
    background_color = fixed_colors[0]

    height = random.randint(16, 22)
    width = random.randint(16, 22)

    input = np.ones((height, width), dtype=int) * background_color
    output = np.ones((height, width), dtype=int) * background_color

    # find three adjact pixels with only background color adjacent to them

    nb_three_shapes = random.randint(2, 5)
    for px in range(nb_three_shapes):
        isolated_position = False
        while not isolated_position:
            x = random.randint(1, width-2)
            y = random.randint(1, height-2)

            # check all pixels within 2 pixels of the current pixel
            all_adjacent = input[y-2:y+2, x-2:x+2]
            if np.any(all_adjacent != background_color):
                continue

            isolated_position = True

        # create 3 adjacent pixels
        three_shape = random.choice([1,2,3])
        if three_shape == 1:
            input[y, x] = fixed_colors[1]
            input[y, x+1] = fixed_colors[1]
            input[y, x-1] = fixed_colors[1]

            output[y, x] = fixed_colors[2]
            output[y, x+1] = fixed_colors[2]
            output[y, x-1] = fixed_colors[2]

        if three_shape == 2:
            input[y, x] = fixed_colors[1]
            input[y+1, x] = fixed_colors[1]
            input[y-1, x] = fixed_colors[1]

            output[y, x] = fixed_colors[2]
            output[y+1, x] = fixed_colors[2]
            output[y-1, x] = fixed_colors[2]

        if three_shape == 3:
            input[y, x] = fixed_colors[1]
            input[y+1, x] = fixed_colors[1]
            input[y+1, x-1] = fixed_colors[1]

            output[y, x] = fixed_colors[2]
            output[y+1, x] = fixed_colors[2]
            output[y+1, x-1] = fixed_colors[2]


    nb_two_shapes = random.randint(3, 6)
    for px in range(nb_two_shapes):
        isolated_position = False
        while not isolated_position:
            x = random.randint(1, width-2)
            y = random.randint(1, height-2)

            # check all pixels within 2 pixels of the current pixel
            all_adjacent = input[y-2:y+2, x-2:x+2]
            if np.any(all_adjacent != background_color):
                continue

            isolated_position = True

        # create 3 adjacent pixels
        two_shape = random.choice([1,2])
        if three_shape == 1:
            input[y, x] = fixed_colors[1]
            input[y, x+1] = fixed_colors[1]

            output[y, x] = fixed_colors[3]
            output[y, x+1] = fixed_colors[3]
           
        if three_shape == 2:
            input[y, x] = fixed_colors[1]
            input[y+1, x] = fixed_colors[1]

            output[y, x] = fixed_colors[3]
            output[y+1, x] = fixed_colors[3]
          

    

    return input, output



def example_func():
    return generate_example