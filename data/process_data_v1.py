import pickle 


SPECIAL_CHARACTERS = {
    # 10 should not be used in a grid, but leave it as a buffer
    "END_ROW": 11,
    "END_GRID": 12,
    "END_EXAMPLE": 13,
    "END_EXAMPLE_SET": 14
}

# TODO: need an "END_EXAMPLE_SET" character to separate example sets

def unpack_grid(grid):
    height = grid.shape[0]
    width = grid.shape[1]
    unpacked_grid = []
    for i in range(height):
        for j in range(width):
            unpacked_grid.append(int(grid[i][j]))
        unpacked_grid.append(SPECIAL_CHARACTERS["END_ROW"])
    return unpacked_grid

def unpack_example_set(example_set, include_end_example_set=True):
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
    if include_end_example_set:
        unpacked_example_set.append(SPECIAL_CHARACTERS["END_EXAMPLE_SET"])
    return unpacked_example_set

        

if __name__ == "__main__":

    rule_name = 'reflect_4'
    
    FLATTENED_EXAMPLE_SETS = []

    with open(f'data/pickled_example_sets/{rule_name}_examples.pkl', 'rb') as f:
        example_sets = pickle.load(f)

    for example_set in example_sets[:]:
        unpacked_set = unpack_example_set(example_set)
        FLATTENED_EXAMPLE_SETS.append(unpacked_set)
        print(len(unpacked_set))