import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_21.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_21.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

import re
from functools import lru_cache


def move(pos, score, x):
    new_pos = (pos + x - 1) % 10 + 1
    score += new_pos
    return new_pos, score


@lru_cache(maxsize=None)
def count_wins(player1, player2):
    if player1[1] >= 21: return (1, 0)
    if player2[1] >= 21: return (0, 1)

    res_p1, res_p2 = 0, 0

    # The possible sums of 3 rolls and how many ways to get them
    for roll_sum, frequency in [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]:
        next_p1 = move(*player1, roll_sum)

        p2_w, p1_w = count_wins(player2, next_p1)

        res_p1 += p1_w * frequency
        res_p2 += p2_w * frequency

    return (res_p1, res_p2)


def process(lines):
    player1 = (int(re.findall(r'\d', lines[0])[1]), 0)
    player2 = (int(re.findall(r'\d', lines[1])[1]), 0)

    return max(count_wins(player1, player2))


print("Sample output:", process(sample_lines))
count_wins.cache_clear()
print("Answer:", process(input_lines))

# pypy ./day_21/part_1.py
