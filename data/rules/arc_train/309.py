import numpy as np
import random

# ARC Public training set 309

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        "fixed_colors": random.sample(range(0, 9), 2),
    }

    return config




def generate_example(config):

    fixed_colors = config["fixed_colors"]
    nb_colors = random.randint(2,4)
    # colors not in fixed_colors
    colors = random.sample([i for i in range(9) if i not in config["fixed_colors"]], nb_colors)

    height = random.randint(3, 6)
    width = random.randint(5, 12)

    input = np.ones((height, width), dtype=int) * fixed_colors[0]
    output = np.ones((height, width), dtype=int) * fixed_colors[0]

    for i in range(height):
        for j in range(width):
            if random.random() < 0.5:
                
                output[i, j] = fixed_colors[1]
            else:
                c = random.choice(colors)
                input[i, j] = c
                output[i, j] = c

    
    

    



    return input, output



def example_func():
    return generate_example