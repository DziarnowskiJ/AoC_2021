import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_8.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_8.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]



def parse(line):
    l, r = line.split(' | ')
    return l.split(), r.split()


def process(lines):
    screens = [parse(line)[1] for line in lines]
    return sum([1 if len(digit) in [2, 3, 4, 7] else 0 for screen in screens
             for digit in screen])



print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_08/part_1.py
