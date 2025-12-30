import itertools
import platform, sys, os
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_5.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_5.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from utils.geometry import *


def parse(lines):
    return [(Point(int(x[0]), -int(x[1])), Point(int(x[2]), -int(x[3])))
            for x in [re.findall(r'\d+', line) for line in lines]]


def process(lines):
    pairs = parse(lines)
    grid = {point: '.' for point in itertools.chain.from_iterable(pairs)}
    grid = {p: int(v) for p, v in empty_grid(*grid_dimensions(grid), char='0').items()}

    for p1, p2 in pairs:
        direct = are_on_same_line(p1, p2, True)
        while isinstance(direct, Direction):
            grid[p1] += 1
            p1 += one_step(direct)
            direct = are_on_same_line(p1, p2, True)
        if isinstance(direct, bool):
            grid[p1] += 1

    points = len([v for v in grid.values() if v > 1])

    return points


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_05/part_1.py
