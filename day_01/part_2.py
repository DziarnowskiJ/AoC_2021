import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_1.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_1.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def process(lines):
    prev = float('inf')
    resp = 0
    for i, line in enumerate(lines[2:]):
        window = sum([int(l) for l in lines[i:i+3]])
        if window > prev:
            resp += 1
        prev = window
    return resp


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_01/part_1.py
