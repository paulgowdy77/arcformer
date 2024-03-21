import datetime
import os
from rule import Rule
import importlib
import pickle
import random
import glob

from process_data_v1 import unpack_example_set

DRY_RUN = False

if not DRY_RUN:

    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M")

    # create a new directory for the dataset
    os.makedirs('data/datasets_v1/' + timestamp)
    # create pickled_examples directory in the new dataset directory
    pickled_examples_dir = 'data/datasets_v1/' + timestamp + '/pickled_examples'
    os.makedirs(pickled_examples_dir)
    # create processed_examples directory in the new dataset directory
    processed_examples_dir = 'data/datasets_v1/' + timestamp + '/processed_examples'
    os.makedirs(processed_examples_dir)


rule_folders = ['data/rules/arc_evaluation/']
#'data/rules/arc_train/', 'data/rules/rules_v1/']

all_rule_filenames = []
for folder in rule_folders:
    all_rule_filenames += glob.glob(folder + '*.py')

all_rule_names = [rule_filename.split('\\')[-1].split('.')[0] for rule_filename in all_rule_filenames]
print("rules:", len(all_rule_names))


EXAMPLE_SETS = 250
EXAMPLES_PER_SET = 4

# split into workable size
split_size = 15000



# pickle example sets
for i, rulle in enumerate(all_rule_names):
    print("Generating: " + rulle + f" ({str(i)})")
    #rule_filename = 'rules.' + rulle
    rule_filename = rulle.replace('/', '.').replace('\\', '.').replace('.py', '')
    rule_filename = rule_filename.replace('data.', '')
    #print("rule_filename:", rule_filename)
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

    out_file = pickled_examples_dir + '/' + rule_filename.split('.')[-1] + '_examples.pkl'

    with open(out_file, 'wb') as f:
        pickle.dump(example_sets, f)

FLATTENED_EXAMPLE_SETS = []
# load pickled example sets and process them
for rule_name in all_rule_names:

    
    rule_name = rule_name.split('/')[-1]
    print("flattening rule:", rule_name)

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

# print the length of all examples combined
print("Number of example sets:", len(FLATTENED_EXAMPLE_SETS))
print("total pixels in all example sets:", sum([len(example_set) for example_set in FLATTENED_EXAMPLE_SETS]))


split_sets = [FLATTENED_EXAMPLE_SETS[i:i + split_size] for i in range(0, len(FLATTENED_EXAMPLE_SETS), split_size)]

# write the processed examples to a file
# with open(f'data/datasets_v1/{timestamp}/processed_examples/processed_examples.pkl', 'wb') as f:
#     pickle.dump(FLATTENED_EXAMPLE_SETS, f)

for i, split_set in enumerate(split_sets):
    # save split set
    with open(f'data/datasets_v1/{timestamp}/processed_examples/processed_examples_{i}.pkl', 'wb') as f:
        pickle.dump(split_set, f)

