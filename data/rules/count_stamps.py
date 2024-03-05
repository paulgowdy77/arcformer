import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'min_height': 18,
        'max_height': 20,
        'min_width': 18,
        'max_width': 20,
    }

    return config

def generate_stamp(bg_color, stamp_color, size=3):
    stamp = np.ones((size, size)) * bg_color
    for i in range(size):
        for j in range(size):
            if random.random() > 0.35:
                stamp[i,j] = stamp_color
    return stamp

def check_proximity(new_point, point_list):
    radius = 3
    for point in point_list:
        if abs(new_point[0] - point[0]) <= 3 and abs(new_point[1] - point[1]) <= 3:
            return False
    return True

def generate_example(config):
    min_height = config['min_height']
    max_height = config['max_height']
    min_width = config['min_width']
    max_width = config['max_width']

    height = random.randint(min_height, max_height)
    width = random.randint(min_width, max_width)


    nb_stamps = random.randint(2, 4)
    colors = random.sample(range(0, 9), nb_stamps+1)
    bg_color = colors[0]
    stamp_colors = colors[1:]
    stamp_counts = random.sample(range(1, 5), nb_stamps)
    stamps = [generate_stamp(bg_color, stamp_colors[i]) for i in range(nb_stamps)]

    input = np.ones((height, width)) * bg_color
    output = stamps[stamp_counts.index(max(stamp_counts))] #np.ones((3,3)) * bg_color


    stamp_centers = []
    for i in range(nb_stamps):

        for j in range(stamp_counts[i]):

            x = random.randint(1, width-2)
            y = random.randint(1, height-2)

            while not check_proximity((x,y), stamp_centers):
                x = random.randint(1, width-2)
                y = random.randint(1, height-2)

            stamp_centers.append((x,y))

            input[y-1:y+2,x-1:x+2] = stamps[i]

    
    return input, output



def example_func():
    return generate_example