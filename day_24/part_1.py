import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_24.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

from z3 import *


def parse(lines):
    blocks = []
    for i in range(14):
        op1 = int(lines[i * 18 + 4].split()[2])
        op2 = int(lines[i * 18 + 5].split()[2])
        op3 = int(lines[i * 18 + 15].split()[2])
        blocks.append([op1, op2, op3])
    return blocks


def pushPop(ks):
    def findPush(j):
        stackSize = 0
        for i in range(j, 0, -1):
            stackSize = stackSize + 1 if ks[i][0] == 26 else stackSize - 1
            if stackSize == 0:
                return i

    pps = []
    for i in range(13):
        if ks[i][0] == 26:
            pps.append([findPush(i), i])
    return pps


def solve(ks):
    opt = Optimize()
    ws = [Int(f"w{i}") for i in range(14)]

    for w in ws:
        opt.add(w >= 1)
        opt.add(w <= 9)

    pairs = pushPop(ks)

    for i, j in pairs:
        opt.add(ws[j] == ws[i] + ks[i][2] + ks[j][1])

    objective_sum = Sum(ws)
    opt.maximize(objective_sum)

    if opt.check() == sat:
        model = opt.model()
        return ''.join([str(model[w]) for w in ws])


def process(lines):
    blocks = parse(lines)

    return solve(blocks)

# See https://observablehq.com/@jwolondon/advent-of-code-2021-day-24?collection=@jwolondon/advent-of-code-2021
print("Answer:", process(input_lines))

# pypy ./day_24/part_1.py
