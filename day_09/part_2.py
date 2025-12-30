import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_9.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_9.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from utils.geometry import *
from utils.search import dijkstra
from functools import reduce
from operator import mul


def process(lines):
    grid = grid_dict(lines)
    grid = {p: v for p,v in grid.items() if v != '9'}
    min_points = []
    for point, val in grid.items():
        if int(val) < min([int(i) for i in get_neighbours_values(point, grid)]):
            min_points.append(point)

    resp = []
    for min_point in min_points:
        _, visited = dijkstra(min_point, Point(-1, -1), grid)
        resp.append(len(visited))

    resp.sort(reverse=True)
    return reduce(mul, resp[:3])


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_09/part_1.py

