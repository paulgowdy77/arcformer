import importlib
import pickle
import os
from rule import Rule

rule_filename = 'rules.majority_fill'

rule_module = importlib.import_module(rule_filename)
config = rule_module.generate_config()
example_func = rule_module.example_func()

rule = Rule(config, example_func)
example = rule.generate_example()

print(example)