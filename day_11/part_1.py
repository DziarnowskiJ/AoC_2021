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
    # First, the energy level of each octopus increases by 1.
    [inc_power(p, grid) for p in grid.keys()]

    # Then, any octopus with an energy level greater than 9 flashes.
    # This increases the energy level of all adjacent octopuses by 1,
    # including octopuses that are diagonally adjacent.
    # If this causes an octopus to have an energy level greater than 9, it also flashes.
    # This process continues as long as new octopuses keep having their energy level increased beyond 9.
    # (An octopus can only flash at most once per step.)
    ready = grid_position('o', grid)
    while len(ready) > 0:
        counter += 1
        pos = ready.pop(0)
        neighbours = get_neighbours_dict(pos, grid)
        for n in neighbours.keys():
            inc_power(n, grid)
            if grid[n] == 'o' and n not in ready:
                ready.append(n)
        grid[pos] = 'x'

    # Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.
    done = grid_position('x', grid)
    for d in done:
        grid[d] = '0'

    return counter



def process(lines):
    grid = grid_dict(lines)
    counter = 0
    for i in range(100):
        counter += step(grid)
    return counter


print("Sample output small:", process(sample_lines_small))
print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_11/part_1.py
