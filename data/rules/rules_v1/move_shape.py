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
            if random.random() > 0.85:
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

    fixed_shape = create_shape_stamp(3, 3, fixed_shape_color, colors[0])
    move_shape = create_shape_stamp(3, 3, colors[1], colors[0])

    # place the fixed shape in the input and output
    x = random.randint(1, width//2 - 1)
    y = random.randint(0, height//2 - 3)
    input[y:y+3, x:x+3] = fixed_shape
    output[y:y+3, x:x+3] = fixed_shape

    
    # place move_shape somewhere below the fixed shape in the input
    # and then move it up to just contact the fixed shape in the output

    x_move = random.randint(x-1, x+1)
    y_move = random.randint(y+3, height-3)
    input[y_move:y_move+3, x_move:x_move+3] = move_shape
    # move the move_shape up to just touch the fixed shape
    output[y+3:y+6,x_move:x_move+3] = move_shape
    
    

    

    # randomly rotate and flip the input and output
    if random.random() > 0.5:
        input = np.rot90(input)
        output = np.rot90(output)
    if random.random() > 0.5:
        input = np.flip(input, 0)
        output = np.flip(output, 0)
    if random.random() > 0.5:
        input = np.rot90(input)
        output = np.rot90(output)
    if random.random() > 0.5:
        input = np.flip(input, 0)
        output = np.flip(output, 0)
    if random.random() > 0.5:
        input = np.rot90(input)
        output = np.rot90(output)
    if random.random() > 0.5:
        input = np.flip(input, 0)
        output = np.flip(output, 0)

    return input, output

def example_func():
    return generate_example