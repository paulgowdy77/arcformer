import numpy as np
import random

def generate_config():
    length_colors = random.sample(range(0, 9), 6)

    config = {
        #'description':  '',

        'nb_examples': 3,

        # 'min_height': 6,
        # 'max_height': 12,
        # 'min_width': 6,
        # 'max_width': 12,

        'background_color': length_colors[0],
        'length_1_color': length_colors[1],
        'length_2_color': length_colors[2],
        'length_3_color': length_colors[3],
        'length_4_color': length_colors[4],
        'input_bar_color': length_colors[5],
    }

    return config


def generate_example(config):

    height = 10
    width = 9

    input = np.ones((height, width)) * config['background_color']
    output = np.ones((height, width)) * config['background_color']

    lengths = random.sample(range(2, 9), 4)
    lengths_sorted = sorted(lengths)

    for i, bar_len in enumerate(lengths):
        color_ind = lengths_sorted.index(bar_len)
        color = config[f'length_{color_ind+1}_color']

        for j in range(bar_len):
            input[height - j - 1, 1 + (i*2)] = config['input_bar_color']
            output[height - j - 1, 1 + (i*2)] = color


    return input, output



def example_func():
    return generate_example