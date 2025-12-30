import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_20.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_20.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from utils.geometry import *


def parse(lines):
    alg = lines[0]
    grid = grid_dict(lines[2:])

    return alg, grid


def get_state(point, grid, alg, default=None):
    default_val = alg[0] if not default else default
    NW = grid.get(point + one_step(Direction.NW), default_val)
    N = grid.get(point + one_step(Direction.N), default_val)
    NE = grid.get(point + one_step(Direction.NE), default_val)
    W = grid.get(point + one_step(Direction.W), default_val)
    O = grid.get(point, default_val)
    E = grid.get(point + one_step(Direction.E), default_val)
    SW = grid.get(point + one_step(Direction.SW), default_val)
    S = grid.get(point + one_step(Direction.S), default_val)
    SE = grid.get(point + one_step(Direction.SE), default_val)

    bin_val = ''.join([NW, N, NE, W, O, E, SW, S, SE]).replace('.', '0').replace('#', '1')

    return alg[int(bin_val, 2)]


def process(lines):
    alg, grid = parse(lines)

    nw, se = grid_dimensions(grid)
    interm_gird = empty_grid(nw + one_step(Direction.NW), se + one_step(Direction.SE))

    for point in interm_gird.keys():
        interm_gird[point] = get_state(point, grid, alg, '.')

    nw, se = grid_dimensions(interm_gird)
    output_gird = empty_grid(nw + one_step(Direction.NW), se + one_step(Direction.SE))

    for point in output_gird.keys():
        output_gird[point] = get_state(point, interm_gird, alg)

    return len(grid_position('#', output_gird))


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_20/part_1.py
