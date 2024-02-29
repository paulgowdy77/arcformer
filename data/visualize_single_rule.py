import importlib
import pickle
import os
from rule import Rule
from plotter_utils import display_example_list

rule_filename = 'rules.corner_fill_reverse'

rule_module = importlib.import_module(rule_filename)
config = rule_module.generate_config()
example_func = rule_module.example_func()


example_set = []

for j in range(4):
    rule = Rule(config, example_func)
    example = rule.generate_example()
    example_set.append(example)

display_example_list(example_set)