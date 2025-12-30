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


def get_state(point, grid, alg, default):
    NW = grid.get(point + one_step(Direction.NW), default)
    N = grid.get(point + one_step(Direction.N), default)
    NE = grid.get(point + one_step(Direction.NE), default)
    W = grid.get(point + one_step(Direction.W), default)
    O = grid.get(point, default)
    E = grid.get(point + one_step(Direction.E), default)
    SW = grid.get(point + one_step(Direction.SW), default)
    S = grid.get(point + one_step(Direction.S), default)
    SE = grid.get(point + one_step(Direction.SE), default)

    bin_val = ''.join([NW, N, NE, W, O, E, SW, S, SE]).replace('.', '0').replace('#', '1')

    return alg[int(bin_val, 2)]


def process(lines):
    alg, grid = parse(lines)

    for i in range(50):
        nw, se = grid_dimensions(grid)
        output_gird = empty_grid(nw + one_step(Direction.NW), se + one_step(Direction.SE))

        for point in output_gird.keys():
            output_gird[point] = get_state(point, grid, alg, '.' if i % 2 == 0 else alg[0])
        grid = output_gird

    return len(grid_position('#', output_gird))


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_20/part_2.py
