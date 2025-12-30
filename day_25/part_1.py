import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_25.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_25.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from utils.geometry import *


def process(lines):
    grid = grid_dict(lines)
    nw, se = grid_dimensions(grid)

    counter = 0
    moved = True
    while moved:
        moved = False
        new_grid = empty_grid(nw, se)
        east = grid_position('>', grid)
        for cuc in east:
            new_x = (cuc.x + 1) % (se.x + 1)
            new_pos = Point(new_x, cuc.y)

            if grid[new_pos] == '.':
                new_grid[new_pos] = '>'
                moved = True
            else:
                new_grid[cuc] = '>'

        south = grid_position('v', grid)
        for cuc in south:
            new_y = cuc.y - 1 if cuc.y > se.y else 0
            new_pos = Point(cuc.x, new_y)

            if new_grid[new_pos] == '.' and grid[new_pos] != 'v':
                new_grid[new_pos] = 'v'
                moved = True
            else:
                new_grid[cuc] = 'v'
        counter += 1

        grid = new_grid

        if counter % 10 == 0:
            print('done', counter)
    return counter


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_25/part_1.py
