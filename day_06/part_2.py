import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_6.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_6.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from itertools import chain


def cycle(val) -> list[int]:
    return [6, 8] if val == 0 else [val - 1]


def process(lines):
    fishes = [int(i) for i in lines[0].split(',')]

    # create fish dict
    # caching dict for resulting state after 128 cycles
    # shows the resulting list and it's length
    fish_dict = {i: [i] for i in range(9)}
    for start, result in fish_dict.items():
        for i in range(128):
            result = list(chain.from_iterable([cycle(val) for val in result]))
        fish_dict[start] = (result, len(result))

    # get states after 128 cycles
    fishes = list(chain.from_iterable([fish_dict[fish][0] for fish in fishes]))
    # instead producing results after next 128 cycles, just get lengths of results
    count = sum([fish_dict[fish][1] for fish in fishes])
    return count


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_06/part_1.py
