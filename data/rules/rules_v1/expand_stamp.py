import numpy as np
import random

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        #'description':  '',

        'nb_examples': 4,

        'input_dim': random.randint(2,4),
        'bg_color': random.randint(0, 9),
    }

    return config


def generate_example(config):
    input_dim = config['input_dim']
    colors = random.sample(range(0, 9), 1)
    while colors[0] == config['bg_color']:
        colors = random.sample(range(0, 9), 1)

    input = np.ones((input_dim, input_dim)) * config['bg_color']
    output = np.ones((input_dim*input_dim, input_dim*input_dim)) * config['bg_color']

    for i in range(input_dim):
        for j in range(input_dim):
            if random.random() > 0.5:
                input[i,j] = colors[0]

    for i in range(input_dim):
        for j in range(input_dim):
            if input[i,j] == colors[0]:
                output[(i*input_dim):(i*input_dim)+input_dim, (j*input_dim):(j*input_dim)+input_dim] = input


    return input, output



def example_func():
    return generate_example