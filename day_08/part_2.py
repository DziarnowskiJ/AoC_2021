import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_8.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_8.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def alphabetic(text):
    sorted_text = [i for i in text]
    sorted_text.sort()
    return ''.join(sorted_text)


def parse(line):
    l, r = line.split(' | ')
    l = [alphabetic(i) for i in l.split()]
    r = [alphabetic(i) for i in r.split()]
    return l, r


def minus(wire1, wire2):
    return ''.join([w for w in wire1 if w not in wire2])


def find_num(search, wires, nums):
    if search == 0:
        val = [i for i in wires if len(i) == 6][0]
    elif search == 1:
        val = [i for i in wires if len(i) == 2][0]
    elif search == 2:
        val = wires[0]
    elif search == 3:
        val = [i for i in wires if len(minus(i, nums[1])) == 3][0]
    elif search == 4:
        val = [i for i in wires if len(i) == 4][0]
    elif search == 5:
        val = [i for i in wires if len(minus(i, nums[6])) == 0 and len(i) == 5][0]
    elif search == 6:
        val = [i for i in wires if len(minus(i, minus(nums[8], nums[7]))) == 2 and len(i) == 6][0]
    elif search == 7:
        val = [i for i in wires if len(i) == 3][0]
    elif search == 8:
        val = [i for i in wires if len(i) == 7][0]
    elif search == 9:
        val = [i for i in wires if len(minus(i, nums[3])) == 1 and len(i) == 6][0]

    wires.remove(val)
    nums[search] = val
    return wires, nums


def find_nums(wires: list[str]) -> dict[int, str]:
    nums = {i: None for i in range(0, 10)}
    search_order = [1, 4, 7, 8, 3, 9, 6, 0, 5, 2]
    for i in search_order:
        wires, nums = find_num(i, wires, nums)

    return nums


def process(lines):
    segments = [parse(line) for line in lines]
    results = []
    for segment in segments:
        num_dict = find_nums(segment[0])
        wire_dict = {val: key for key, val in num_dict.items()}
        result = []
        for i in segment[1]:
            result.append(wire_dict[i])
        results.append(''.join([str(i) for i in result]))
    return sum([int(i) for i in results])


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_08/part_1.py
