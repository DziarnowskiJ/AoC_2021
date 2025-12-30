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


def shoot(h, v):
    x_pos = 0
    y_pos = 0
    max_y = 0
    while y_pos >= y_lb and x_pos <= x_ub:
        x_pos += h
        h = max(h - 1, 0)
        y_pos += v
        v -= 1
        max_y = max(max_y, y_pos)
        if x_lb <= x_pos <= x_ub and y_lb <= y_pos <= y_ub:
            return max_y
    return 0


def process(lines):
    global x_lb, x_ub, y_lb, y_ub
    x_lb, x_ub, y_lb, y_ub = parse(lines)

    y_range = (y_lb, abs(y_lb))
    x_range = (min([i for i in range(x_lb // 2) if sum(x for x in range(i)) >= x_lb]) - 1, x_ub + 1)

    return max(shoot(h, v)
               for h in range(*x_range)
               for v in range(*y_range))


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_17/part_1.py
