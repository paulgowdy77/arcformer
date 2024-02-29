import numpy as np
import random

def generate_config():
    config = {
        "fixed_shape_color": random.choice([0,1,2,3,4,5,6,7,8,9]),
    }
    return config


def create_shape_stamp(height, width, color, bg_color):
    shape = np.ones((height, width)) * color
    for i in range(height):
        for j in range(width):
            if random.random() < 0.15:
                shape[i, j] = bg_color
    return shape


def generate_example(config):

    fixed_shape_color = config["fixed_shape_color"]

    colors = random.sample([0,1,2,3,4,5,6,7,8,9], 2)
    # make sure the colors are different
    while fixed_shape_color in colors:
        colors = random.sample([0,1,2,3,4,5,6,7,8,9], 2)

    height = random.randint(12, 20)
    width = random.randint(12, 20)

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    fixed_shape = create_shape_stamp(4, 4, fixed_shape_color, colors[0])
    move_shape = create_shape_stamp(4, 4, colors[1], colors[0])

    # place the fixed shape in the input and output
    x = random.randint(0, width//2 - 4)
    y = random.randint(0, height//2 - 4)
    input[y:y+4, x:x+4] = fixed_shape
    output[y:y+4, x:x+4] = fixed_shape

    # fix x
    # place move shape below the fixed shape in the output
    output[y+4:y+8, x:x+4] = move_shape

    # move the shape down a bit in the input
    # determine how far to move the shape down
    move_distance = random.randint(1, height//2-4)
    input[y+4+move_distance:y+8+move_distance, x:x+4] = move_shape

    

    


   

    return input, output

def example_func():
    return generate_example