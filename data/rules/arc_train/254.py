import numpy as np
import random

# ARC Public training set 254

def generate_config():
    length_colors = random.sample(range(0, 9), 6)

    config = {

        # 'min_height': 6,
        # 'max_height': 12,
        # 'min_width': 6,
        # 'max_width': 12,

        'background_color': length_colors[0],
        'max_color': length_colors[1],
        'min_color': length_colors[2],

        'input_bar_color': length_colors[3],
    }

    return config


def generate_example(config):

    height = 10
    width = 9

    input = np.ones((height, width)) * config['background_color']
    output = np.ones((height, width)) * config['background_color']

    min_color = config['min_color']
    max_color = config['max_color']

    lengths = random.sample(range(2, 9), 4)
    lengths_sorted = sorted(lengths)

    max_length = lengths_sorted[-1]
    min_length = lengths_sorted[0]

    for i, bar_len in enumerate(lengths):

        for j in range(bar_len):
            input[height - j - 1, 1 + (i*2)] = config['input_bar_color']

            if bar_len == min_length:
                output[height - j - 1, 1 + (i*2)] = min_color
            if bar_len == max_length:
                output[height - j - 1, 1 + (i*2)] = max_color


    return input, output

    return input, output



def example_func():
    return generate_example