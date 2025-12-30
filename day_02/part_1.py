import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_2.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_2.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def process(lines):
    horiz, depth = 0, 0
    for (comm, val) in [line.split() for line in lines]:
        if comm == 'forward':
            horiz += int(val)
        elif comm == 'down':
            depth += int(val)
        elif comm == 'up':
            depth -= int(val)

    return horiz * depth


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_02/part_1.py
