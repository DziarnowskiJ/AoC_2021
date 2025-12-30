import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_12.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_12.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_12_small.txt', 'r') as file:
    sample_lines_small = [i.rstrip("\n") for i in file.readlines()]


class Cave:
    def __init__(self, name):
        self.name = name
        self.is_small = not name.isupper()

    def __repr__(self):
        return f"<Cave: {self.name}, is_small: {self.is_small}>"


from copy import deepcopy


def parse(lines):
    return [item
            for line in lines
            for x, y in [line.split('-')]
            for item in [(Cave(x), Cave(y)),
                         (Cave(y), Cave(x))]]


def get_moves(curr, conns) -> list[Cave]:
    return [x[1] for x in conns if x[0].name == curr.name]


def change(curr: Cave, nxt: Cave, conns: list[tuple[Cave, Cave]]):
    new_conns = deepcopy(conns)
    if curr.is_small:
        new_conns = [conn for conn in new_conns if conn[0].name != curr.name and conn[1].name != curr.name]
    return nxt, new_conns


def check_done(cave: Cave):
    return cave.name == 'end'


def check_paths(curr: Cave, conns: list[tuple[Cave, Cave]]):
    if check_done(curr):
        return 1
    else:
        moves = get_moves(curr, conns)
        return sum([check_paths(*change(curr, move, conns)) for move in moves])


def process(lines):
    conns = parse(lines)
    curr = Cave('start')
    # moves = get_moves(curr, conns)

    return check_paths(curr, conns)


print("Sample output small:", process(sample_lines_small))
print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_12/part_1.py
