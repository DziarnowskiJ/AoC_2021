import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_11.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_11.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_11_small.txt', 'r') as file:
    sample_lines_small = [i.rstrip("\n") for i in file.readlines()]

from utils.geometry import *


def inc_power(point, grid):
    val = grid[point]
    if val not in ['x', 'o']:
        if val == '9':
            grid[point] = 'o'
        else:
            grid[point] = str(int(val) + 1)


def step(grid):
    counter = 0
    # Energy level of each octopus increases by 1.
    [inc_power(p, grid) for p in grid.keys()]

    # Each ready octopus flashed
    ready = grid_position('o', grid)
    while len(ready) > 0:
        counter += 1
        pos = ready.pop(0)
        neighbours = get_neighbours_dict(pos, grid)
        # Flash increases energy of adjacent octopuses
        for n in neighbours.keys():
            inc_power(n, grid)
            # Octopus may become ready to flash
            if grid[n] == 'o' and n not in ready:
                ready.append(n)
        grid[pos] = 'x'

    # Reset state of octopuses that flashed
    done = grid_position('x', grid)
    for d in done:
        grid[d] = '0'

    return len(done) == len(grid.keys())


def process(lines):
    grid = grid_dict(lines)
    counter = 0
    all_flashed = False
    while not all_flashed:
        all_flashed = step(grid)
        counter += 1
    return counter


print("Sample output small:", process(sample_lines_small))
print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_11/part_1.py
