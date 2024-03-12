import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 20,
        'max_height': 24,
        'min_width': 20,
        'max_width': 24,

        'colors': random.sample(range(0,9), 3)
    }

    return config

def check_overlap_margin_1(boxes, box_top, box_left, box_height, box_width):
    for box in boxes:
        if box_top - 1 <= box[0] + box[2] and box_top + box_height + 1 >= box[0] and box_left - 1 <= box[1] + box[3] and box_left + box_width + 1 >= box[1]:
            return False

    return True

def generate_box(height, width, nb_dots, color1, color2):
    box = np.ones((height, width)) * color1

    dots = random.sample(range(0, height * width), nb_dots)

    for dot in dots:
        box[dot // width, dot % width] = color2

    return box


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

    nb_boxes = random.randint(4, 6)
    nb_dots = [random.randint(2,5) for i in range(nb_boxes)]
    min_ind = random.randint(0, nb_boxes-1)
    nb_dots[min_ind] = min(nb_dots) - 1
    boxes = []

    # randomly place boxes with no overlap
    for i in range(nb_boxes):
        box_height = random.randint(3, 4)
        box_width = random.randint(2, 5)

        box_top = random.randint(0, height - box_height)
        box_left = random.randint(0, width - box_width)

        while not check_overlap_margin_1(boxes, box_top, box_left, box_height, box_width):
            #print("overlapping")
            box_height = random.randint(3, 4)
            box_width = random.randint(2, 5)

            box_top = random.randint(0, height - box_height)
            box_left = random.randint(0, width - box_width)


        boxes.append((box_top, box_left, box_height, box_width))

        box = generate_box(box_height, box_width, nb_dots[i], colors[1], colors[2])

        input[box_top:box_top+box_height, box_left:box_left+box_width] = box
        if i != min_ind:
            output[box_top:box_top+box_height, box_left:box_left+box_width] = box
        


    return input, output



def example_func():
    return generate_example