import numpy as np
import random

def generate_config():
    config = {
    }
    return config

def generate_example(config):

    colors = random.sample(range(0, 9), 3)
    grid_number = random.randint(3, 4)
    grid_size = 3 #random.randint(3, 5)

    grid_count = grid_number * grid_number
    dot_counts = [random.randint(0, 5) for _ in range(grid_count)]
    # make sure there's one clear max dot count
    max_dot_count = max(dot_counts)
    max_dot_count_index = dot_counts.index(max_dot_count)
    dot_counts[max_dot_count_index] = max_dot_count + 1

    size = grid_number * grid_size + grid_number - 1

    input = np.ones((size, size)) * colors[0]

    # draw grid lines
    for i in range(1, grid_number):
        input[i * grid_size + i - 1, :] = colors[1]
        input[:, i * grid_size + i - 1] = colors[1]

    output = input.copy()

    # draw dots
    # place random dots in the input grid
    for i in range(grid_count):
        x = i % grid_number
        y = i // grid_number
        x_start = x * grid_size + x
        y_start = y * grid_size + y
        x_end = x_start + grid_size
        y_end = y_start + grid_size
        dot_count = dot_counts[i]
        for j in range(dot_count):
            dot_x = random.randint(x_start, x_end - 1)
            dot_y = random.randint(y_start, y_end - 1)
            # make sure we're not overlapping dots
            while input[dot_y, dot_x] == colors[2]:
                dot_x = random.randint(x_start, x_end - 1)
                dot_y = random.randint(y_start, y_end - 1)
            input[dot_y, dot_x] = colors[2]
        # if this is the max dot count, fill this output grid with the max color
        if i == max_dot_count_index:
            output[y_start:y_end, x_start:x_end] = colors[2]

    
    # randomly flip the input and output grids
    # otherwise there will be a bias for earlier grids to have the max dot count
    if random.random() > 0.5:
        input = np.flip(input, 0)
        output = np.flip(output, 0)
   
    return input, output



def example_func():
    return generate_example