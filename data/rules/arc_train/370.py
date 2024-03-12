import numpy as np
import random

# ARC Public training set 370
# ISSUE: doesnt spill over the board edge

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
    }

    return config


def generate_example(config):

    colors = random.sample(range(0, 9), 3)

    height = random.randint(14, 24)
    width = random.randint(14, 24)

    input = np.ones((height, width), dtype=int) * colors[0]
    output = np.ones((height, width), dtype=int) * colors[0]

    stamp_height = random.randint(3, 5)
    stamp_width = random.randint(3, 5)

    rect_stamp = np.ones((stamp_height, stamp_width), dtype=int) * colors[0]
    colored_rect_stamp = rect_stamp.copy()
    for i in range(stamp_height):
        for j in range(stamp_width):
            if random.random() < 0.45:
                rect_stamp[i, j] = colors[1]
                colored_rect_stamp[i, j] = colors[2]

            # make sure edges are colored
            if i == 0 or i == stamp_height - 1 or j == 0 or j == stamp_width - 1:
                if random.random() < 0.85:
                    rect_stamp[i, j] = colors[1]
                    colored_rect_stamp[i, j] = colors[2]

    central_x = random.randint(4, width - 4 - stamp_width)
    central_y = random.randint(4, height - 4 - stamp_height)

    input[central_y:central_y+stamp_height, central_x:central_x+stamp_width] = rect_stamp
    output[central_y:central_y+stamp_height, central_x:central_x+stamp_width] = rect_stamp

 
    # pick a direction

    direction = random.choice(["up", "down", "left", "right", "up_left", "up_right", "down_left", "down_right"])
    # tile colored_rect_stamp in the direction in the output    
    # repeat colored_rect_stamp in the direction as many times as possible, and make it run off the edge
    # of the output

    if direction == "up":
        # put a row of pixels above the stamp in the input
        for i in range(stamp_width):
            input[central_y - 1, central_x + i] = colors[2]
        for i in range(1, 5):
            if central_y - i * stamp_height >= 0:
                output[central_y - i * stamp_height:central_y - (i - 1) * stamp_height, central_x:central_x+stamp_width] = colored_rect_stamp
    elif direction == "down":
        # put a row of pixels below the stamp in the input
        for i in range(stamp_width):
            input[central_y + stamp_height, central_x + i] = colors[2]
        for i in range(1, 5):
            if central_y + (i + 1) * stamp_height <= height:
                output[central_y + i * stamp_height:central_y + (i + 1) * stamp_height, central_x:central_x+stamp_width] = colored_rect_stamp
    elif direction == "left":
        # put a column of pixels to the left of the stamp in the input
        for i in range(stamp_height):
            input[central_y + i, central_x - 1] = colors[2]
        for i in range(1, 5):
            if central_x - i * stamp_width >= 0:
                output[central_y:central_y+stamp_height, central_x - i * stamp_width:central_x - (i - 1) * stamp_width] = colored_rect_stamp
    elif direction == "right":
        # put a column of pixels to the right of the stamp in the input
        for i in range(stamp_height):
            input[central_y + i, central_x + stamp_width] = colors[2]
        for i in range(1, 5):
            if central_x + (i + 1) * stamp_width <= width:
                output[central_y:central_y+stamp_height, central_x + i * stamp_width:central_x + (i + 1) * stamp_width] = colored_rect_stamp
    elif direction == "up_left":
        # put a pixel to the upper left of the stamp in the input
        input[central_y - 1, central_x - 1] = colors[2]
        for i in range(1, 5):
            if central_x - i * stamp_width >= 0 and central_y - i * stamp_height >= 0:
                output[central_y - i * stamp_height:central_y - (i - 1) * stamp_height, central_x - i * stamp_width:central_x - (i - 1) * stamp_width] = colored_rect_stamp
    elif direction == "up_right":
        # put a pixel to the upper right of the stamp in the input
        input[central_y - 1, central_x + stamp_width] = colors[2]
        for i in range(1, 5):
            if central_x + (i + 1) * stamp_width <= width and central_y - i * stamp_height >= 0:
                output[central_y - i * stamp_height:central_y - (i - 1) * stamp_height, central_x + i * stamp_width:central_x + (i + 1) * stamp_width] = colored_rect_stamp
    elif direction == "down_left":
        # put a pixel to the lower left of the stamp in the input
        input[central_y + stamp_height, central_x - 1] = colors[2]
        for i in range(1, 5):
            if central_x - i * stamp_width >= 0 and central_y + (i + 1) * stamp_height <= height:
                output[central_y + i * stamp_height:central_y + (i + 1) * stamp_height, central_x - i * stamp_width:central_x - (i - 1) * stamp_width] = colored_rect_stamp
    elif direction == "down_right":
        # put a pixel to the lower right of the stamp in the input
        input[central_y + stamp_height, central_x + stamp_width] = colors[2]
        for i in range(1, 5):
            if central_x + (i + 1) * stamp_width <= width and central_y + (i + 1) * stamp_height <= height:
                output[central_y + i * stamp_height:central_y + (i + 1) * stamp_height, central_x + i * stamp_width:central_x + (i + 1) * stamp_width] = colored_rect_stamp
    


    return input, output



def example_func():
    return generate_example