import numpy as np
import random

# ARC Public training set 179

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
    }

    return config



def generate_example(config):

    colors = random.sample(range(0, 9), 4)

    dim = (2 * random.randint(3, 6)) - 1

    input = np.ones((dim, dim), dtype=int) * colors[0]
    
    for i in range(dim):
        for j in range(dim):
            input[i, j] = random.choice(colors)

    # mirror inptu along diagonal
    output = np.zeros((dim, dim), dtype=int)
    for i in range(dim):
        for j in range(dim):
            output[i, j] = input[j, i]

    
   
    



    return input, output



def example_func():
    return generate_example