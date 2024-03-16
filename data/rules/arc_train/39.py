import numpy as np
import random

# ARC Public training set 39
# DONE

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
    }

    return config


def generate_example(config):

    output_size = random.choice([3, 4, 5])
    colors = random.sample(range(0, 9), 5)
    output = np.ones((output_size, output_size), dtype=int) * colors[0]
    input_size = random.randint(10, 16)
    input = np.ones((input_size, input_size), dtype=int) * colors[0]

    for i in range(output_size):
        for j in range(output_size):
            if random.random() < 0.45:
                output[i, j] = random.choice(colors)

    # create rotated stamp from output
    stamp = np.zeros((output_size*2, output_size*2), dtype=int)
    stamp[0:output_size, 0:output_size] = output
    stamp[output_size:, 0:output_size] = np.flipud(output)
    stamp[0:output_size, output_size:] = np.fliplr(output)
    stamp[output_size:, output_size:] = np.flipud(np.fliplr(output))


    # add stamp to input
    stamp_top = random.randint(0, input_size-output_size*2)
    stamp_left = random.randint(0, input_size-output_size*2)

    input[stamp_top:stamp_top+output_size*2, stamp_left:stamp_left+output_size*2] = stamp

    return input, output



def example_func():
    return generate_example