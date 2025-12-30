import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_7.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_7.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

import math
from utils.lists import transpose


def process(lines):
    positions = [int(i) for i in lines[0].split(',')]
    start, end = min(positions), max(positions)
    costs = []
    for pos in positions:
        costs.append([math.fsum(range(1, abs(pos - i) + 1)) for i in range(start, end)])

    cost = min([sum(i) for i in transpose(costs)])
    return int(cost)


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_07/part_1.py
