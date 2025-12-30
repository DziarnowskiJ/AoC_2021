import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_10.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_10.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

openings = ['(', '[', '{', '<']
closings = [')', ']', '}', '>']

matching = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

scoring = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def check_line(line):
    heap = []
    for i in line:
        if i in openings:
            heap.append(i)
        elif i in closings:
            val = heap.pop(-1)
            if matching[val] != i:
                return scoring[i]
    return 0


def process(lines):
    return sum([check_line(line) for line in lines])


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_10/part_1.py
