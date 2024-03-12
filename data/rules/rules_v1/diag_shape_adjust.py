import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {

        'nb_examples': 4,

        'min_height': 16,
        'max_height': 18,
        'min_width': 16,
        'max_width': 18,
    }

    return config

def check_overlapping(top_left, shape_width, shape_height, top_lefts, widths, heights):

    for i, current_point in enumerate(top_lefts):


        if top_left[0]-1 > current_point[0] and top_left[0]-1 < current_point[0] + heights[i]:
            if top_left[1] > current_point[1] and top_left[1] < current_point[1] + widths[i]:
                return True

    return False # not overlapping



def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)

    colors = random.sample(range(0, 9), 3)

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]

    #generate 2 pairs of lines that dont overlap
    # then connect the top points
    nb_shapes = random.choice([1,1])

    top_lefts = []
    widths = []
    heights = []

    for n in range(nb_shapes):
        #generate 2 points
        shape_height = random.randint(2, 5)
        shape_width = random.randint(2, 5)
        top_left = (random.randint(1, height-shape_height-2), random.randint(1, width-1-2*max(shape_width,shape_height)))
        top_right = (top_left[0] - 1, top_left[1] + shape_width)
        #p2 = (random.randint(0, height-1), random.randint(0, width-1))

        while check_overlapping(top_left, shape_width, shape_height, top_lefts, widths, heights):
            shape_height = random.randint(2, 5)
            shape_width = random.randint(2, 5)
            top_left = (random.randint(1, height-shape_height-2), random.randint(1, width-1-2*max(shape_width,shape_height)))
            top_right = (top_left[0] - 1, top_left[1] + shape_width)



        input_points = [top_left, top_right]
        output_points = [top_left, top_right]

        for i in range(shape_width):
            input_points.append((top_left[0]-1, top_left[1]+i))
            input_points.append((top_left[0] + shape_height, top_left[1]+shape_height + i + 1))
            #points.append((top_right[0], top_right[1]+i))
            output_points.append((top_left[0]-1, top_left[1]+i))
            output_points.append((top_left[0] + shape_height, top_left[1]+shape_height + i -1))

        for i in range(1,shape_height+1):
            input_points.append((top_left[0] + i, top_left[1]+i))
            input_points.append((top_right[0] + i, top_right[1]+i))

            if i < shape_height - 2:
                output_points.append((top_left[0] + i, top_left[1]+i))
                output_points.append((top_right[0] + i, top_right[1]+i))
            else:
                output_points.append((top_left[0] + i, top_left[1] + shape_height - 2))
                output_points.append((top_right[0] + i, top_right[1] + shape_height - 2))



        for p in input_points:
            input[p[0], p[1]] = colors[n+1]
            #output[p[0], p[1]] = colors[n+1]
        for p in output_points:
            #input[p[0], p[1]] = colors[n+1]
            output[p[0], p[1]] = colors[n+1]
   

    return input, output



def example_func():
    return generate_example