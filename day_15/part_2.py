import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_15.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_15.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

import math
from utils.geometry import *
from utils.search import dijkstra_weighted


def expand_grid(grid, grid_size):
    new_grid = {}
    new_grid.update(grid)
    for p, v in grid.items():
        for i in range(0, 5):
            for j in range(0, 5):
                val = (int(v) + (1 * i) + (1 * j))
                while val > 9:
                    val -= 9
                new_grid[Point(int(p.x + (grid_size * i)), int(p.y - (grid_size * j)))] = str(val)
    return new_grid


def process(lines):
    grid = grid_dict(lines)
    grid_size = math.sqrt(len(grid))
    new_grid = expand_grid(grid, grid_size)
    nw, se = grid_dimensions(new_grid)
    path, visited = dijkstra_weighted(nw, se, new_grid)
    return sum([int(new_grid[p]) for p in path[1:]])


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_15/part_1.py
