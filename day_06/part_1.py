import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_6.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_6.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

import itertools


def cycle(val) -> list[int]:
    return [6, 8] if val == 0 else [val - 1]


def process(lines):
    fishes = [int(i) for i in lines[0].split(',')]
    for i in range(12):
        fishes = list(itertools.chain.from_iterable([cycle(val) for val in fishes]))
    # return fishes
    return len(fishes)


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_06/part_1.py
