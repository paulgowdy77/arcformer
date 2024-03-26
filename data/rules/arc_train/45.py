import numpy as np
import random

# ARC Public training set 45
# matching colors connect

# could do rotations
# can it handle different rotations across an example set?

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
    }

    return config


def generate_example(config):

    colors = random.sample(range(0, 9), 7)

    width = random.randint(12,16)
    height = random.randint(12,16)

    input = np.ones((width, height), dtype=int) * colors[0]
    output = np.ones((width, height), dtype=int) * colors[0]

    nb_lines = random.randint(3, 5)
    nb_matches = random.randint(1, 2)
    match_indices = random.sample(range(0, nb_lines), nb_matches)

    # identify line positions along width
    # line positions should be seperated by at least 1 pixel
    # and one pixel off from the start and end of the width
    line_positions = [1+x*2 for x in range(nb_lines)]

    for line_nb in range(nb_lines):

        left_color = random.choice(colors[1:])

        if line_nb in match_indices:
            # match
            right_color = left_color
            input[line_positions[line_nb], 0] = left_color
            input[line_positions[line_nb], -1] = right_color
            output[line_positions[line_nb], :] = left_color
        else:
            right_color = random.choice(colors[1:])
            while right_color == left_color:
                right_color = random.choice(colors[1:])
            input[line_positions[line_nb], 0] = left_color
            input[line_positions[line_nb], -1] = right_color
            output[line_positions[line_nb], 0] = left_color
            output[line_positions[line_nb], -1] = right_color


    

    
    return input, output



def example_func():
    return generate_example