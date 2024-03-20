import numpy as np
import random

# ARC Public eval set 52

def generate_config():

    config = {
        'fixed_colors': random.sample(range(0, 9), 2),
        'nb_rotations': random.randint(0, 3)
    }

    return config


def generate_example(config):
    fixed_colors = config['fixed_colors']
    dot_colors = [c for c in range(9) if c not in fixed_colors]
    random.shuffle(dot_colors)

    height = random.randint(14,20)
    width = random.randint(14,20)

    input = np.ones((height, width)) * fixed_colors[0]
    output = np.ones((height, width)) * fixed_colors[0]

    remove_color = dot_colors[0]

    for i in range(height):
        for j in range(width):
            if random.random() > 0.75:
                random_dot_color = random.choice(dot_colors)
                input[i,j] = random_dot_color

                if random_dot_color != remove_color:
                    output[i,j] = random_dot_color

    input[:4,:4] = fixed_colors[1]
    output[:4,:4] = fixed_colors[1]
    input[:3,:3] = fixed_colors[0]
    output[:3,:3] = fixed_colors[0]

    input[1,1] = remove_color
    output[1,1] = remove_color

    for _ in range(config['nb_rotations']):
        input = np.rot90(input)
        output = np.rot90(output)

    

    return input, output



def example_func():
    return generate_example