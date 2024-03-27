import numpy as np
import random

# ARC Public training set 346

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        "fixed_colors": random.sample(range(0, 9), 1),
    }

    return config


def generate_example(config):
    
    bg_color = config["fixed_colors"][0]
    # make 2 colors not in fixed_colors
    colors = random.sample([x for x in range(9) if x != bg_color], 2)

    width = random.randint(8, 14)
    height = random.randint(8,14)

    input = np.ones((height, width), dtype=int) * bg_color

    for i in range(height):
        for j in range(width):
            if random.random() < 0.25:
                input[i, j] = random.choice(colors)

    selected = False
    while not selected:
        for i in range(1,height-1):
            for j in range(1,width-1):
                if input[i, j] == colors[0]:
                    if random.random() < 0.05:
                        # surround this pixel with the other color
                        input[i-1, j-1] = colors[1]
                        input[i-1, j] = colors[1]
                        input[i-1, j+1] = colors[1]
                        input[i, j-1] = colors[1]
                        input[i, j+1] = colors[1]
                        input[i+1, j-1] = colors[1]
                        input[i+1, j] = colors[1]
                        input[i+1, j+1] = colors[1]
                        
                        selected = True
    output = np.ones((1,1), dtype=int) * colors[0]
                



  
    return input, output



def example_func():
    return generate_example