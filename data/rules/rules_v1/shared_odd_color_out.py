import numpy as np
import random

def generate_config():
    config = {
        "nb_examples": 4,
        'colors': random.sample(range(0,9), 7)
    }
    return config

def generate_multicolor_stamp(bg_color, colors):
    stamp = np.ones((3, 3), dtype=int) * bg_color
    nb_colors = len(colors)
    random.shuffle(colors)
    positions = random.sample(range(0,8), nb_colors)

    for i, p in enumerate(positions):
        x = p % 3
        y = p // 3
        stamp[y, x] = colors[i]

    return stamp

def generate_example(config):
    colors = config['colors']
    input = np.zeros((11, 11)) * colors[0]
    output = np.ones((1,1)) * colors[6]


    for i in range(11):
        input[i,3] = colors[1]
        input[i,7] = colors[1]
        input[3,i] = colors[1]
        input[7,i] = colors[1]

    four_color = random.randint(0,8)

    for i in range(3):
        for j in range(3):
            if (i*3) + j == four_color:
                stamp = generate_multicolor_stamp(colors[0], colors[2:6])
            else:
                stamp = generate_multicolor_stamp(colors[0], colors[2:7])
            input[i*3 + i : i*3 + 3 + i, j*3 + j : j*3+3 + j] = stamp


    return input, output

def example_func():
    return generate_example