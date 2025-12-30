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
    for num_line in board:
        num_line.remove(val) if val in num_line else num_line


def check_win(boards: list[list]):
    return [board for board in boards if any([len(b) == 0 for b in board])]


def process(lines):
    numbers, boards = parse(lines)
    transposed_boards = [transpose(board) for board in boards]
    all_boards = boards + transposed_boards

    for i in numbers:
        for board in all_boards:
            remove_val(board, i)
            win = check_win(all_boards)
            if win:
                return sum(list(itertools.chain.from_iterable(win[0]))) * i


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_04/part_1.py
