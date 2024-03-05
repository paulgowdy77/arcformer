import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

    }

    return config


def generate_stamp(colors):
    s = np.ones((3,3)) * colors[0]
    s[1,1] = colors[1]

    qs = [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1), (2,2)]

    patches = [[],[],[]]

    for q in qs:

        if random.random() > 0.15:

            i = random.randint(2,4)
            s[q] = colors[i]
            patches[i-2].append(q)


    zz = []
    for i, p in enumerate(patches):
        z = np.ones((3,3)) * colors[0]
        z[1,1] = colors[1]
        for q in p:
            z[q] = colors[i+2]
        if len(p) > 0:
            zz.append(z)

    return s, zz

def check_points(r,c,old_points):
    for p in old_points:
        if abs(r-p[0]) < 3 or abs(c-p[1]) < 3:
            return False
    return True


def generate_example(config):


    height = 16 #random.randint(min_height, max_height)
    width = 16 #random.randint(min_width, max_width)

    colors = random.sample(range(0, 9), 5)

    input = np.ones((height, width)) * colors[0]


    output, stamp_fragments = generate_stamp(colors)

    old_points = [(-2,-2)]

    for sf in stamp_fragments:
        r = random.randint(2,height-2)
        c = random.randint(2,width-2)

        while not check_points(r,c,old_points):
            r = random.randint(2,height-2)
            c = random.randint(2,width-2)

        old_points.append((r,c))

        input[r-1:r+2,c-1:c+2] = sf

    return input, output



def example_func():
    return generate_example