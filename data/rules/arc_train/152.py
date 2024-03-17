import numpy as np
import random

# ARC Public training set 117

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
    }

    return config




def generate_example(config):
    
    colors = random.sample(range(0, 9), 8)
    input_dim = random.randint(3, 5)
    input = np.ones((input_dim, input_dim), dtype=int) * colors[0]
    output = np.ones((input_dim*2, input_dim*2), dtype=int) * colors[0]

    for i in range(input_dim):
        for j in range(input_dim):
            if random.random() < 0.85:
                input[i, j] = random.choice(colors)

    # flip the input and put it in the output
    output[:input_dim, :input_dim] = input
    output[input_dim:, :input_dim] = np.flipud(input)
    output[:input_dim, input_dim:] = np.fliplr(input)
    output[input_dim:, input_dim:] = np.fliplr(np.flipud(input))

    return input, output



def example_func():
    return generate_example