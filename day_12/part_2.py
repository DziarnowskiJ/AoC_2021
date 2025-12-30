import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_12.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_12.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_12_small.txt', 'r') as file:
    sample_lines_small = [i.rstrip("\n") for i in file.readlines()]
with open(base_path + '/inputs/sample/sample_input_day_12_xsmall.txt', 'r') as file:
    sample_lines_xsmall = [i.rstrip("\n") for i in file.readlines()]

from copy import deepcopy
from functools import lru_cache

class Cave:
    def __init__(self, name):
        self.name = name
        self.is_small = not self.name.isupper()

    def __repr__(self):
        # return f"<Cave: {self.name}, is_small: {self.is_small}>"
        return self.name



def parse(lines) -> tuple[tuple[Cave, Cave]]:
    return tuple([item
            for line in lines
            for x, y in [line.split('-')]
            for item in [(Cave(x), Cave(y)),
                         (Cave(y), Cave(x))]])


@lru_cache()
def get_moves(curr: Cave, conns: tuple[tuple[Cave, Cave]]) -> tuple[Cave]:
    return tuple([x[1] for x in conns if x[0].name == curr.name])


@lru_cache()
def change(curr: Cave, nxt: Cave, conns: tuple[tuple[Cave, Cave]], special_name: [Cave or str]) \
        -> tuple[Cave, tuple[tuple[Cave, Cave]], [Cave or str]]:
    new_conns = deepcopy(conns)
    new_curr = deepcopy(curr)
    new_conns = [deepcopy(conn) for conn in new_conns if conn[0].name != curr.name and conn[1].name != curr.name]

    from_conns = []
    to_conns = []

    is_special = new_curr.name == special_name
    if not new_curr.is_small or is_special:
        if is_special:
            special_name = ''
        from_conns = [tuple([new_curr, deepcopy(conn[1])]) for conn in conns if conn[0].name == new_curr.name]
        to_conns = [tuple([deepcopy(conn[0]), new_curr]) for conn in conns if conn[1].name == new_curr.name]

    new_conns = tuple(new_conns + from_conns + to_conns)

    return nxt, new_conns, special_name


def check_done(cave: Cave):
    return cave.name == 'end'

@lru_cache(maxsize=None)
def check_paths(curr: Cave, conns: tuple[tuple[Cave, Cave]], special: [Cave or str]) -> list[tuple[Cave, ...]]:
    if check_done(curr):
        return [(curr.name, )]

    else:
        all_paths = []
        for move in get_moves(curr, conns):
            nxt, conns, special = change(curr, move, conns, special)
            paths = check_paths(nxt, conns, special)

            for path in paths:
                new_path = (curr.name,) + path
                all_paths.append(new_path)

        return all_paths


def process(lines):
    conns = parse(lines)
    smalls = list(set([x for line in lines
              for x in line.split('-')
              if x.islower() and x not in ['start', 'end']]))

    curr = Cave('start')

    paths = []
    for small in smalls:
        paths += check_paths(curr, deepcopy(conns), small)

    return len(set(paths))


print("Sample output small:", process(sample_lines_xsmall))
print("Sample output small:", process(sample_lines_small))
print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_12/part_2.py
