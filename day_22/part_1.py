import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_22.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_22_small.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

import re


def parse(lines: list[str]):
    commands = []
    for line in lines:
        turn_on = line.startswith('on')
        vals = re.findall(r'-?\d+', line)
        x_range = range(int(vals[0]), int(vals[1]) + 1)
        y_range = range(int(vals[2]), int(vals[3]) + 1)
        z_range = range(int(vals[4]), int(vals[5]) + 1)

        commands.append((turn_on, x_range, y_range, z_range))
    return commands


def process(lines):
    commands = parse(lines)

    lights = set()
    for command in commands:
        if command[0]:
            lights.update({(x, y, z)
                           for x in command[1] if -50 <= x <= 50
                           for y in command[2] if -50 <= y <= 50
                           for z in command[3] if -50 <= z <= 50})
        elif not command[0]:
            lights = lights.difference({(x, y, z)
                               for x in command[1] if -50 <= x <= 50
                               for y in command[2] if -50 <= y <= 50
                               for z in command[3] if -50 <= z <= 50})

    return len(lights)


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_22/part_1.py
