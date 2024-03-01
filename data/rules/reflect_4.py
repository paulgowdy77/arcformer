import numpy as np
import random

def generate_config():
    config = {
        "input_dim": random.choice([3,3,4,4,5])
    }
    return config




def generate_example(config):
    input_dim = config["input_dim"]

    colors = random.sample([0,1,2,3,4,5,6,7,8,9], 4)

    input = np.ones((input_dim, input_dim)) * colors[0]

    for i in range(input_dim):
        for j in range(input_dim):
            if random.random() > 0.5:
                input[i, j] = random.choice(colors[1:])

    output = np.ones((2*input_dim, 2*input_dim)) * colors[0]

    output[0:input_dim, 0:input_dim] = input
    # reflect the input shape
    output[0:input_dim, input_dim:input_dim*2] = np.fliplr(input)
    output[input_dim:input_dim*2, 0:input_dim] = np.flipud(input)
    output[input_dim:input_dim*2, input_dim:input_dim*2] = np.fliplr(np.flipud(input))


    return input, output

def example_func():
    return generate_example