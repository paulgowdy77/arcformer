import pickle 
from plotter_utils import display_example_list
import random

rule = 'half_fill'

with open(f'data/pickled_example_sets/{rule}_examples.pkl', 'rb') as f:
    example_sets = pickle.load(f)

print(len(example_sets))

example = random.choice(example_sets)

display_example_list(example)