import numpy as np
import random

# ARC Public training set 368

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        "fixed_colors": random.sample(range(0, 9), 2)
    }

    return config


def generate_example(config):

    fixed_colors = config['fixed_colors']
    nb_colors = random.randint(2, 4)
    # sample colors not in fixed_colors
    colors = random.sample([c for c in range(9) if c not in fixed_colors], nb_colors)

    height = random.randint(14, 24)
    width = random.randint(14, 24)

    input = np.ones((height, width), dtype=int) * fixed_colors[0]
    output = np.ones((height, width), dtype=int) * fixed_colors[0]

    rect_height = random.randint(3, 5)
    rect_width = random.randint(3, 5)

    rect_stamp = np.ones((rect_height, rect_width), dtype=int) * fixed_colors[1]

    colored_rect_stamp = rect_stamp.copy()
    for i in range(rect_height):
        for j in range(rect_width):
            colored_rect_stamp[i, j] = colors[random.randint(0, nb_colors - 1)]

    nb_rects = random.randint(2, 4)

    # generate rectangle positions that don't overlap
    positions = []
    for _ in range(nb_rects):
        x = random.randint(0, width - rect_width)
        y = random.randint(0, height - rect_height)
        while any([x < x2 + rect_width and x + rect_width > x2 and y < y2 + rect_height and y + rect_height > y2 for x2, y2 in positions]):
            x = random.randint(0, width - rect_width)
            y = random.randint(0, height - rect_height)
        positions.append((x, y))

    for x, y in positions:
        output[y:y+rect_height, x:x+rect_width] = colored_rect_stamp
        input[y:y+rect_height, x:x+rect_width] = rect_stamp

    input[y:y+rect_height, x:x+rect_width] = colored_rect_stamp


    return input, output



def example_func():
    return generate_example