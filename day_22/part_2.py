import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_22.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_22_large.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

import re


def parse(lines: list[str]):
    commands = []
    for line in lines:
        turn_on = line.startswith('on')
        vals = re.findall(r'-?\d+', line)
        x_range = (int(vals[0]), int(vals[1]))
        y_range = (int(vals[2]), int(vals[3]))
        z_range = (int(vals[4]), int(vals[5]))

        commands.append((turn_on, x_range, y_range, z_range))
    return commands


def process(lines):
    commands = parse(lines)

    cuboids = []

    for is_on, x_range, y_range, z_range in commands:
        new_intersections = []

        for cx_range, cy_range, cz_range, weight in cuboids:
            ix1 = max(x_range[0], cx_range[0])
            ix2 = min(x_range[1], cx_range[1])
            iy1 = max(y_range[0], cy_range[0])
            iy2 = min(y_range[1], cy_range[1])
            iz1 = max(z_range[0], cz_range[0])
            iz2 = min(z_range[1], cz_range[1])

            if ix1 <= ix2 and iy1 <= iy2 and iz1 <= iz2:
                new_intersections.append(((ix1, ix2), (iy1, iy2), (iz1, iz2), -weight))

        cuboids.extend(new_intersections)
        if is_on:
            cuboids.append((x_range, y_range, z_range, 1))

    total_on = 0
    for x_range, y_range, z_range, weight in cuboids:
        volume = (x_range[1] - x_range[0] + 1) * (y_range[1] - y_range[0] + 1) * (z_range[1] - z_range[0] + 1)
        total_on += volume * weight

    return total_on


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_22/part_1.py
