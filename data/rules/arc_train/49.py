import numpy as np
import random

# ARC Public training set 49
# KNOWN ISSUE: if the a larger rectangle is partly obscured but doesnt go through to the other side, it might appear smaller overall
# need to check for this

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
    }

    return config


def generate_example(config):

    colors = random.sample(range(0, 9), 7)

    width = random.randint(16,24)
    height = random.randint(16,24)

    nb_rects = random.randint(3, 5)

    rect_shapes = []

    for rect in range(nb_rects):
        w = random.randint(2, 10)
        h = random.randint(2, 10)
        area = w * h
        rect_shapes.append([area, w, h])

    # sort rects by area
    rect_shapes = sorted(rect_shapes, key=lambda x: x[0])
    min_area = rect_shapes[0][0]
    # make sure there's only one min area
    rect_shapes = [rect_shapes[0]] + [x for x in rect_shapes if x[0] != min_area]
    # reverse sort
    rect_shapes = rect_shapes[::-1]
    input = np.ones((width, height), dtype=int) * colors[0]

    for i, rect in enumerate(rect_shapes):
        w = rect[1]
        h = rect[2]

        color = colors[i]
        x = random.randint(0, width - w)
        y = random.randint(0, height - h)
        input[x:x+w, y:y+h] = color

    min_rect = rect_shapes[-1]
    w = min_rect[1]
    h = min_rect[2]
    output = np.ones((w, h), dtype=int) * color

    return input, output



def example_func():
    return generate_example