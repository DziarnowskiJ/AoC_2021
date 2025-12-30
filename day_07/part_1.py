import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_7.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_7.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from statistics import median


def process(lines):
    positions = [int(i) for i in lines[0].split(',')]
    change = [int(abs(pos - median(positions))) for pos in positions]

    return sum(change)


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_07/part_1.py
