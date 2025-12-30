import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_21.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_21.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

import re


class Player:
    def __init__(self, pos):
        self.pos = pos
        self.score = 0

    def __str__(self):
        return f'Player: {self.pos}, {self.score}'

    def move(self, x):
        new_pos = (self.pos + x) % 10
        val = 10 if new_pos == 0 else new_pos
        self.pos = val
        self.score += val


class Dice:
    val = 0
    throw_count = 0

    def throw(self):
        val = self.val + 1
        new_val = val % 100
        show_val = 100 if new_val == 0 else new_val
        self.val = show_val
        self.throw_count += 1
        return show_val


def process(lines):
    player1 = Player(int(re.findall(r'\d', lines[0])[1]))
    player2 = Player(int(re.findall(r'\d', lines[1])[1]))
    dice = Dice()

    while True:
        move_count = sum([dice.throw(), dice.throw(), dice.throw()])
        player1.move(move_count)
        if player1.score >= 1000:
            return player2.score * dice.throw_count
        move_count = sum([dice.throw(), dice.throw(), dice.throw()])
        player2.move(move_count)
        if player2.score >= 1000:
            return player1.score * dice.throw_count


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_21/part_1.py
