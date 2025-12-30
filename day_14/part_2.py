import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_14.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_14.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

import re
from collections import Counter
from operator import add
from functools import reduce


def parse(lines):
    template = lines.pop(0)
    lines.pop(0)
    subs = {x: y for line in lines
            for x, y in [line.split(' -> ')]}

    return template, subs


def get_insertion(match):
    key = match.group(1) + match.group(2)
    return match.group(1) + subs[key]


def get_pairs(text):
    return [''.join([text[i], text[i + 1]]) for i in range(len(text) - 1)]


def get_sub_result(sub):
    for i in range(20):
        sub = re.sub(pattern=r'(.)(?=(.))', repl=get_insertion, string=sub)
    return Counter(sub[:-1])


def process(lines):
    global subs
    template, subs = parse(lines)

    # produce result after 20 iterations and split it into pairs
    for i in range(20):
        template = re.sub(pattern=r'(.)(?=(.))', repl=get_insertion, string=template)
    result_pairs = get_pairs(template)

    # create a lookup dict for each pair after 20 iterations
    subs_dict = {sub: get_sub_result(sub) for sub in subs.keys()}

    # instead of running 20 more iterations, use lookup dict to determine
    # number of letters for each pair
    # This simulates running the original text for 40 iterations
    master_counter = reduce(add, [subs_dict[p] for p in result_pairs])

    # get_sub_result removes last value because it is the first value of the next pair
    # because of it, last value of the original string needs to be added back
    master_counter[template[-1]] += 1

    # Find most and least common letter
    most_common = master_counter.most_common(1)[0][1]
    least_common = master_counter.most_common(len(master_counter))[-1][1]

    return most_common - least_common


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_14/part_1.py
