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
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}


def check_line(line):
    heap = []
    for i in line:
        if i in openings:
            heap.append(i)
        elif i in closings:
            val = heap.pop(-1)
            if matching[val] != i:
                return None
    result = 0
    for cls in reversed(heap):
        result *= 5
        result += scoring[cls]
    return result


def process(lines):
    checks = [check_line(line) for line in lines]
    checks = [check for check in checks if check is not None]
    checks.sort()
    return checks[len(checks)//2]


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_10/part_1.py
