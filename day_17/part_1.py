import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_17.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_17.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

import re


def parse(lines):
    x0, x1, y0, y1 = re.findall(r'-?\d+', lines[0])
    return int(x0), int(x1), int(y0), int(y1)


def process(lines):
    _, _, y, _ = parse(lines)
    return sum(range(0, abs(y)))


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_17/part_1.py
