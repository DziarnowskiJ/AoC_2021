import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_3.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_3.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from utils.lists import transpose


def swap(x):
    # Swap 0 to 1 and 1 to 0
    return str(abs(int(x) - 1))


def process(lines):
    lines = transpose([[l for l in line] for line in lines])

    most_common = []
    for line in lines:
        most_common.append(max(line, key=line.count))

    least_common = [swap(x) for x in most_common]

    mc = int(''.join(most_common), 2)
    lc = int(''.join(least_common), 2)
    return mc * lc


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_03/part_1.py
