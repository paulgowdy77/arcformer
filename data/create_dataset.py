import datetime
import os
from rule import Rule
import importlib
import pickle
import random

from process_data_v1 import unpack_example_set

timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M")

# create a new directory for the dataset
os.makedirs('data/datasets_v1/' + timestamp)
# create pickled_examples directory in the new dataset directory
pickled_examples_dir = 'data/datasets_v1/' + timestamp + '/pickled_examples'
os.makedirs(pickled_examples_dir)
# create processed_examples directory in the new dataset directory
processed_examples_dir = 'data/datasets_v1/' + timestamp + '/processed_examples'
os.makedirs(processed_examples_dir)

rules = [
    'corner_fill_reverse',
    'corner_fill',
    'expand_two_by_two',
    'half_fill_dot',
    'half_fill',
    'majority_fill',
    'move_dots_one_in_direction',
    'move_shape',
    'reflect_4_reverse',
    'reflect_4',
    'seperate_odd_color_out',
    'shared_odd_color_out'
]

EXAMPLE_SETS = 500
EXAMPLES_PER_SET = 4

# pickle example sets
for rulle in rules:
    print("Generating: " + rulle)
    rule_filename = 'rules.' + rulle
    rule_module = importlib.import_module(rule_filename)
    config = rule_module.generate_config()
    example_func = rule_module.example_func()

    example_sets = []

    for i in range(EXAMPLE_SETS):
        example_set = []
        for j in range(EXAMPLES_PER_SET):
            rule = Rule(config, example_func)
            example = rule.generate_example()
            example_set.append(example)
        example_sets.append(example_set)

    out_file = pickled_examples_dir + '/' + rule_filename.split('.')[1] + '_examples.pkl'

    with open(out_file, 'wb') as f:
        pickle.dump(example_sets, f)

FLATTENED_EXAMPLE_SETS = []
# load pickled example sets and process them
for rule_name in rules:

    with open(f'data/datasets_v1/{timestamp}/pickled_examples/{rule_name}_examples.pkl', 'rb') as f:
        example_sets = pickle.load(f)

    for example_set in example_sets[:]:

        unpacked_set = unpack_example_set(example_set)
        FLATTENED_EXAMPLE_SETS.append(unpacked_set)

        #shuffle the examples
        random.shuffle(example_set)
        unpacked_set = unpack_example_set(example_set)
        FLATTENED_EXAMPLE_SETS.append(unpacked_set)

random.shuffle(FLATTENED_EXAMPLE_SETS)

