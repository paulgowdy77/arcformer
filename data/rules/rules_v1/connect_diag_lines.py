import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 14,
        'max_height': 20,
        'min_width': 14,
        'max_width': 20,
    }

    return config


def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)
    

    nb_of_lines = random.randint(1,4)

    colors = random.sample(range(0, 9), 1 + nb_of_lines)

    input = np.ones((height, width)) * colors[0]
    output = np.ones((height, width)) * colors[0]


    all_points = []

    for i in range(nb_of_lines):

        line_drawn = False 

        while not line_drawn:
            line_length = random.randint(3,7)
            line_direction = random.choice([[1,1], [1,-1], [-1,1], [-1,-1]])
            line_start = random.randint(0, height-1), random.randint(0, width-1)

            line_points = [line_start]

            for j in range(line_length):
                new_point = line_points[j][0] + line_direction[0], line_points[j][1] + line_direction[1]
                if new_point[0] < 0 or new_point[0] >= height or new_point[1] < 0 or new_point[1] >= width:
                    break
                line_points.append(new_point)
  
            
            # if all points safe, line is safe, can draw it and move on
            p = [x not in all_points for x in line_points]
            if all(p) and len(line_points) > 2:
                all_points.extend(line_points)
                
                line_drawn = True
                # draw line
                for k, point in enumerate(line_points):
                    output[point] = colors[i+1]
                    if k in [0, len(line_points)-1]:
                        input[point] = colors[i+1]


    return input, output



def example_func():
    return generate_example