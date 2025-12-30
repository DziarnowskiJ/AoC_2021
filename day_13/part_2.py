import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_13.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_13.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from utils.geometry import *
import re


def parse(lines):
    empty = lines.index('')

    points = [Point(int(x), -int(y))
              for line in lines[:empty]
              for x, y in [line.split(',')]]

    folds = [(fold, int(val) * (1 if fold == 'x' else -1)) for line in lines[empty + 1:]
             for fold in [re.findall(r'[yx]', line)[0]]
             for val in [re.findall(r'\d+', line)[0]]]

    return points, folds

def fold_grid(points, fold_axis, fold_val):
    new_points = set()
    for point in points:
        if fold_axis == 'y':
            if point.y > fold_val:
                new_points.add(point)
            else:
                dist = point.y - fold_val
                new_points.add(Point(point.x, fold_val - dist))
        if fold_axis == 'x':
            if point.x < fold_val:
                new_points.add(point)
            else:
                dist = point.x - fold_val
                new_points.add(Point(fold_val - dist, point.y))

    return new_points

def make_grid(points):
    grid = {p: '█' for p in points}
    full_grid = empty_grid(*grid_dimensions(grid))
    full_grid.update(grid)
    return full_grid

def process(lines):
    points, folds = parse(lines)
    for fold in folds:
        points = fold_grid(points, *fold)

    full_grid = make_grid(points)

    return '\n'+points_to_text(full_grid)


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_13/part_1.py
