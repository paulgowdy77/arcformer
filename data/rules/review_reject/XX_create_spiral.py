import numpy as np
import random

def generate_config():
    config = {
        'colors': random.sample(range(0, 9), 2),
    }
    return config

def generate_example(config):
    colors = config['colors']

    input_width = random.randint(14, 20)
    input_height = random.randint(14, 20)

    input = np.ones((input_height, input_width)) * colors[0]
    output = np.ones((input_height, input_width)) * colors[0]

    i = 0
    j = 0

    
    

    


   
    return input, output



def example_func():
    return generate_example