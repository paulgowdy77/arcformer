import importlib
import pickle
import os
from rule import Rule
from plotter_utils import display_example_list

rule_filename = 'rules.seperate_odd_color_out'

rule_module = importlib.import_module(rule_filename)
config = rule_module.generate_config()
example_func = rule_module.example_func()

EXAMPLE_SETS = 10
EXAMPLES_PER_SET = 4

example_sets = []

for i in range(EXAMPLE_SETS):
    example_set = []
    for j in range(EXAMPLES_PER_SET):
        rule = Rule(config, example_func)
        example = rule.generate_example()
        example_set.append(example)
    example_sets.append(example_set)

out_file = 'data/pickled_example_sets/' + rule_filename.split('.')[1] + '_examples.pkl'

with open(out_file, 'wb') as f:
    pickle.dump(example_sets, f)