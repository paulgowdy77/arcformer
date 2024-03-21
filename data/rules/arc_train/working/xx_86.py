import numpy as np
import random

# ARC Public training set 86

def generate_config():
    #colors = random.sample(range(0, 9), 2)

    config = {
    }

    return config




def generate_example(config):

    colors = random.sample(range(0, 9), 3)

    dim = random.randint(16,22)
    input = np.ones((dim, dim), dtype=int) * colors[0]
    output = np.ones((dim, dim), dtype=int) * colors[0]

    nb_blooms = random.randint(1,3)

    bloom_size_dict = {
        1: 1+1+1,
        2: 2+1+2,
        3: 3+1+3
    }

    for i in range(nb_blooms):

        overlapping = True
        while overlapping:
            bloom_inner_size = random.choice([1,1,1,2,2,3])
            bloom_x = random.randint(0, dim-1-bloom_size_dict[bloom_inner_size])
            bloom_y = random.randint(0, dim-1-bloom_size_dict[bloom_inner_size])
            if np.any(input[bloom_x:bloom_x+bloom_size_dict[bloom_inner_size], bloom_y:bloom_y+bloom_size_dict[bloom_inner_size]] != colors[0]):
                overlapping = True
            else:
                overlapping = False

        # bloom total size
        total_bloom_size = bloom_size_dict[bloom_inner_size]
        print(bloom_inner_size, total_bloom_size)

        bloom_input_stamp = np.ones((total_bloom_size, total_bloom_size), dtype=int) * colors[0]
        bloom_output_stamp = np.ones((total_bloom_size, total_bloom_size), dtype=int) * colors[0]


        
        bloom_input_stamp[bloom_inner_size:total_bloom_size-bloom_inner_size, bloom_inner_size:total_bloom_size-bloom_inner_size] = colors[1]
        bloom_input_stamp[bloom_inner_size+1:total_bloom_size-bloom_inner_size-1, bloom_inner_size+1:total_bloom_size-bloom_inner_size-1] = colors[2]
        


        # bloom_output_stamp[:,:] = colors[2]
        # bloom_output_stamp[bloom_inner_size:total_bloom_size-bloom_inner_size, bloom_inner_size:total_bloom_size-bloom_inner_size] = colors[1]

        input[bloom_x:bloom_x+total_bloom_size, bloom_y:bloom_y+total_bloom_size] = bloom_input_stamp
        #output[bloom_x:bloom_x+total_bloom_size, bloom_y:bloom_y+total_bloom_size] = bloom_output_stamp


    

    return input, output



def example_func():
    return generate_example