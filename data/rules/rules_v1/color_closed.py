import numpy as np
import random

def generate_config():
    colors = random.sample(range(0, 9), 3)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 14,
        'max_height': 18,
        'min_width': 14,
        'max_width': 18,

        'colors': colors,
    }

    return config

def no_overlap(boxes, box_y, box_x, box_height, box_width):
    for y, x, height, width in boxes:
        if box_y + box_height> y and box_y < y + height:
            if box_x + box_width > x and box_x < x + width:
                return False
    return True

def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    colors = config['colors']

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    #generate non overlapping boxes
    num_boxes = random.randint(1, 4)
    boxes = []
    while len(boxes) < num_boxes:
        box_height = random.randint(4,6)
        box_width = random.randint(3, 6)
        box_y = random.randint(0, height - box_height)
        box_x = random.randint(0, width - box_width)
        if no_overlap(boxes, box_y, box_x, box_height, box_width):
            boxes.append((box_y, box_x, box_height, box_width))

    # color random pixels outside of all boxes
    for i in range(height):
        for j in range(width):
            if random.random() < 0.1:
                if no_overlap(boxes, i, j, 1, 1):
                    input[i, j] = colors[1]
                    output[i, j] = colors[1]
        

    for box_y, box_x, box_height, box_width in boxes:

        if random.randint(0,1) == 1:


            for i in range(box_height):
                #if random.random() < 0.98:
                input[box_y + i, box_x] = colors[1]
                input[box_y + i, box_x + box_width - 1] = colors[1]
                output[box_y + i, box_x] = colors[2]
                output[box_y + i, box_x + box_width - 1] = colors[2]


            for j in range(box_width):
                #if random.random() < 0.98:
                input[box_y, box_x + j] = colors[1]
                input[box_y + box_height - 1, box_x + j] = colors[1]
                output[box_y, box_x + j] = colors[2]
                output[box_y + box_height - 1, box_x + j] = colors[2]

        else:

            for i in range(box_height):
                if random.random() < 0.75:
                    input[box_y + i, box_x] = colors[1]
                    input[box_y + i, box_x + box_width - 1] = colors[1]
                    output[box_y + i, box_x] = colors[1]
                    output[box_y + i, box_x + box_width - 1] = colors[1]
                else:
                    input[box_y + i, box_x] = colors[0]
                    input[box_y + i, box_x + box_width - 1] = colors[0]
                    output[box_y + i, box_x] = colors[0]
                    output[box_y + i, box_x + box_width - 1] = colors[0]


            for j in range(box_width):
                if random.random() < 0.75:
                    input[box_y, box_x + j] = colors[1]
                    input[box_y + box_height - 1, box_x + j] = colors[1]
                    output[box_y, box_x + j] = colors[1]
                    output[box_y + box_height - 1, box_x + j] = colors[1]
                else:
                    input[box_y, box_x + j] = colors[0]
                    input[box_y + box_height - 1, box_x + j] = colors[0]
                    output[box_y, box_x + j] = colors[0]
                    output[box_y + box_height - 1, box_x + j] = colors[0]



    return input, output



def example_func():
    return generate_example