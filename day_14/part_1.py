import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_14.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_14.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

import re
from collections import Counter


def parse(lines):
    template = lines.pop(0)
    lines.pop(0)
    subs = {x: y for line in lines
            for x, y in [line.split(' -> ')]}

    return template, subs


def get_insertion(match):
    key = match.group(1) + match.group(2)
    return match.group(1) + subs[key]


def process(lines):
    global subs
    template, subs = parse(lines)

    for i in range(10):
        template = re.sub(pattern=r'(.)(?=(.))', repl=get_insertion, string=template)

    freq_dict = Counter(template)
    most_common = freq_dict.most_common(1)[0][1]
    least_common = freq_dict.most_common(len(freq_dict))[-1][1]

    return most_common - least_common


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_14/part_1.py
