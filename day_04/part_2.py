import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_4.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_4.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from utils.lists import transpose
import itertools


def parse(lines):
    numbers = [int(val) for val in lines.pop(0).split(',')]

    boards = []
    board = []
    pointer = 1
    lines.pop(0)
    for line in lines:
        if pointer % 6 == 0:
            boards.append(board)
            board = []
            pointer += 1
            continue
        pointer += 1
        board.append([int(i) for i in line.split()])
    boards.append(board)

    return numbers, boards


def remove_val(board, val):
    return [['x' if item == val else item for item in num_line] for num_line in board]


def check_win(boards: list[list]):
    return [i for i, board in enumerate(boards) if any([all(x == 'x' for x in line) for line in board + transpose(board)])]

def score_board(board, i):
    return sum([x for x in itertools.chain.from_iterable(board) if x != 'x']) * i

def process(lines):
    numbers, boards = parse(lines)

    last_board = None
    last_i = 0
    while len(boards) > 0:
        i = numbers.pop(0)
        boards = [remove_val(board, i) for board in boards]
        win = check_win(boards)
        if len(win) > 0:
            win.sort(reverse=True)
            for w in win:
                last_board = boards.pop(w)
                last_i = i
    return score_board(last_board, last_i)


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_04/part_1.py
