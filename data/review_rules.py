import glob
from rule import Rule
from plotter_utils import display_example_list
import importlib

rule_files = glob.glob('data/rules_2/arc_data_mac_3_3_24/*.py')


def visualize_rule(rule_filename):
    rule_module = importlib.import_module(rule_filename)
    config = rule_module.generate_config()
    example_func = rule_module.example_func()

    example_set = []

    for j in range(4):
        rule = Rule(config, example_func)
        example = rule.generate_example()
        example_set.append(example)

    display_example_list(example_set)

for rule_file in rule_files[:10]:
    rule_filename = rule_file.split('/')[-1].split('.')[0]
    rule_name = rule_filename.split('\\')[-1]
    print(rule_name)
    rule_name = 'rules_2.arc_data_mac_3_3_24.' + rule_name

    for i in range(3):
        visualize_rule(rule_name)

