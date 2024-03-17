import numpy as np
import random

# ARC Public training set 325

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
    }

    return config

def generate_stamp(size, bg_color, fg_color):
    stamp = np.ones((size, size))*bg_color
    hits = 0
    while hits < 2:
        for i in range(size):
            for j in range(size):
                if random.random() < 0.85:
                    hits += 1
                    stamp[i, j] = fg_color

    # make sure there are no lone pixels
    for i in range(size):
        for j in range(size):
            if i > 0 and i < size-1 and j > 0 and j < size-1:
                if stamp[i, j] == fg_color:
                    if stamp[i-1, j] == bg_color and stamp[i+1, j] == bg_color and stamp[i, j-1] == bg_color and stamp[i, j+1] == bg_color:
                        stamp[i, j] = bg_color
            # check border as well
            if i == 0 and j > 0 and j < size-1:
                if stamp[i, j] == fg_color:
                    if stamp[i+1, j] == bg_color and stamp[i, j-1] == bg_color and stamp[i, j+1] == bg_color:
                        stamp[i, j] = bg_color
            if i == size-1 and j > 0 and j < size-1:
                if stamp[i, j] == fg_color:
                    if stamp[i-1, j] == bg_color and stamp[i, j-1] == bg_color and stamp[i, j+1] == bg_color:
                        stamp[i, j] = bg_color
            if j == 0 and i > 0 and i < size-1:
                if stamp[i, j] == fg_color:
                    if stamp[i-1, j] == bg_color and stamp[i+1, j] == bg_color and stamp[i, j+1] == bg_color:
                        stamp[i, j] = bg_color
            if j == size-1 and i > 0 and i < size-1:
                if stamp[i, j] == fg_color:
                    if stamp[i-1, j] == bg_color and stamp[i+1, j] == bg_color and stamp[i, j-1] == bg_color:
                        stamp[i, j] = bg_color

            if i == 0 and j == 0:
                if stamp[i, j] == fg_color:
                    if stamp[i+1, j] == bg_color and stamp[i, j+1] == bg_color:
                        stamp[i, j] = bg_color
            if i == 0 and j == size-1:
                if stamp[i, j] == fg_color:
                    if stamp[i+1, j] == bg_color and stamp[i, j-1] == bg_color:
                        stamp[i, j] = bg_color
            if i == size-1 and j == 0:
                if stamp[i, j] == fg_color:
                    if stamp[i-1, j] == bg_color and stamp[i, j+1] == bg_color:
                        stamp[i, j] = bg_color
            if i == size-1 and j == size-1:
                if stamp[i, j] == fg_color:
                    if stamp[i-1, j] == bg_color and stamp[i, j-1] == bg_color:
                        stamp[i, j] = bg_color
    return stamp


def generate_example(config):

    colors = random.sample(range(0, 9), 2)

    nb_stamps = random.randint(1, 5)

    input_dim = 3*nb_stamps + 5

    input = np.ones((input_dim, input_dim), dtype=int) * colors[0]
    output = np.ones((nb_stamps,nb_stamps), dtype=int) * colors[0]

    for i in range(nb_stamps):
        stamp_placed = False
        while not stamp_placed:
            stamp_size = random.randint(2, 4)
            stamp = generate_stamp(stamp_size, colors[0], colors[1])
            # place the stamp in a non-overlapping non-touching way
            
            #pick a random x,y
            x = random.randint(1, input_dim - stamp_size)
            y = random.randint(1, input_dim - stamp_size)

            # check if the whole stamp size can be placed with a margin of 1
            if np.any(input[x-1:x+stamp_size+1, y-1:y+stamp_size+1] != colors[0]):
                continue
        
            input[x:x+stamp_size, y:y+stamp_size] = stamp
            output[i, i] = colors[1]
            stamp_placed = True
        

    



    return input, output



def example_func():
    return generate_example