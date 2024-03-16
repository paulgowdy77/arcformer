import numpy as np
import random

# ARC Public training set 332
# DONE

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
        "fixed_colors": random.sample(range(0, 9), 1),
    }

    return config


def generate_example(config):
    
    fixed_colors = config["fixed_colors"]
    # make 2 colors not in fixed_colors
    colors = random.sample([x for x in range(9) if x not in fixed_colors], 2)

    width = random.randint(8, 16)
    height = random.randint(3,5)


    input = np.ones((height, width), dtype=int) * colors[0]
    output = np.ones((height, width), dtype=int) * colors[0]

    for i in range(height):
        for j in range(width):
            if random.random() < 0.35:
                input[i, j] = colors[1]

                if j % 2 == 0:
                    output[i, j] = fixed_colors[0]
                else:
                    output[i, j] = colors[1]

  
    return input, output



def example_func():
    return generate_example