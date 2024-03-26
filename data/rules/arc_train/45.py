import numpy as np
import random

# ARC Public training set 45
# matching colors connect

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
    }

    return config


def generate_example(config):

    colors = random.sample(range(0, 9), 7)

    width = random.randint(8,12)
    height = random.randint(8,12)

    nb_lines = random.randint(3, 6)
    nb_matches = random.randint(1, 3)
    match_indices = random.sample(range(0, nb_lines), nb_matches)

    # identify line positions along width
    # line positions should be seperated by at least 1 pixel
    # and one pixel off from the start and end of the width
    line_positions = [1+x*2 for x in range(nb_lines)]

    for line_nb in range(nb_lines):

        left_color = 

        if line_nb in match_indices:
            # match
            color = colors[0]

    

    
    return input, output



def example_func():
    return generate_example