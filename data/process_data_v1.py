import pickle 

rule_name = 'half_fill'

with open(f'data/pickled_example_sets/{rule_name}_examples.pkl', 'rb') as f:
    example_sets = pickle.load(f)

FLATTENED_EXAMPLE_SETS = []

SPECIAL_CHARACTERS = {
    # 10 should not be used in a grid, but leave it as a buffer
    "END_ROW": 11,
    "END_GRID": 12,
    "END_EXAMPLE": 13,
}

def unpack_grid(grid):
    height = grid.shape[0]
    width = grid.shape[1]
    unpacked_grid = []
    for i in range(height):
        for j in range(width):
            unpacked_grid.append(int(grid[i][j]))
        unpacked_grid.append(SPECIAL_CHARACTERS["END_ROW"])
    return unpacked_grid

def unpack_example_set(example_set):
    unpacked_example_set = []
    for example in example_set:
        # each example is a dict with input and output keys
        unpacked_INPUT_grid = unpack_grid(example['input'])
        unpacked_example_set.extend(unpacked_INPUT_grid)
        unpacked_example_set.append(SPECIAL_CHARACTERS["END_GRID"])
        unpacked_OUTPUT_grid = unpack_grid(example['output'])
        unpacked_example_set.extend(unpacked_OUTPUT_grid)
        unpacked_example_set.append(SPECIAL_CHARACTERS["END_GRID"])
        unpacked_example_set.append(SPECIAL_CHARACTERS["END_EXAMPLE"])
    return unpacked_example_set

        

for example_set in example_sets[:1]:
    unpacked_set = unpack_example_set(example_set)
    FLATTENED_EXAMPLE_SETS.append(unpacked_set)

print(FLATTENED_EXAMPLE_SETS[0])