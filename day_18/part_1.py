import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_18.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

sample_lines = dict()
for i in range(1, 6):
    with open(base_path + f'/inputs/sample/sample_input_day_18_{i}.txt', 'r') as file:
        sample_lines[i] = [i.rstrip("\n") for i in file.readlines()]


def find_path_to_depth(item, target_depth, current_depth=1):
    if current_depth == target_depth:
        return []

    if isinstance(item, list):
        for i, sub_item in enumerate(item):
            path = find_path_to_depth(sub_item, target_depth, current_depth + 1)

            if path is not None:
                return [i] + path
    return None


def find_path_to_split(item):
    if isinstance(item, int) and item > 9:
        return []

    if isinstance(item, list):
        for i, sub_item in enumerate(item):
            path = find_path_to_split(sub_item)

            if path is not None:
                return [i] + path
    return None


def get_val(number, path):
    n = number
    for i in path:
        n = n[i]
    return n


def replace_val(number, path, repl):
    if not path:
        return

    target = number
    for i in path[:-1]:
        target = target[i]

    target[path[-1]] = repl


def increment_left_after_path(number, path, val):
    last_right = -1
    for i, direction in enumerate(path):
        if direction == 1:
            last_right = i

    if last_right == -1: return  # No left neighbor exists

    parent = number
    for i in range(last_right):
        parent = parent[path[i]]

    idx = 0
    curr = parent[idx]

    while isinstance(curr, list):
        parent = curr
        idx = 1
        curr = curr[idx]

    parent[idx] += val


def increment_right_after_path(number, path, val):
    last_left = -1
    for i, direction in enumerate(path):
        if direction == 0:
            last_left = i

    if last_left == -1: return  # No right neighbor exists

    parent = number
    for i in range(last_left):
        parent = parent[path[i]]

    idx = 1
    curr = parent[idx]

    while isinstance(curr, list):
        parent = curr
        idx = 0
        curr = curr[idx]

    parent[idx] += val


def reduction(number):
    # print(number)
    exploding_path = find_path_to_depth(number, 6)
    split_path = find_path_to_split(number)

    if exploding_path:
        pair_path = exploding_path[:-1]
        left_path = pair_path + [0]
        right_path = pair_path + [1]

        left_val = get_val(number, left_path)
        right_val = get_val(number, right_path)

        increment_left_after_path(number, pair_path, left_val)
        increment_right_after_path(number, pair_path, right_val)
        replace_val(number, pair_path, 0)

        return reduction(number)
    elif split_path:
        split_val = get_val(number, split_path)
        l_split = split_val // 2
        r_split = (split_val + 1) // 2
        replace_val(number, split_path, [l_split, r_split])

        return reduction(number)

    return number


def get_magnitude(number):
    if isinstance(number, int):
        return number

    return get_magnitude(number[0]) * 3 + get_magnitude(number[1]) * 2


def process(lines):
    numbers = [eval(line) for line in lines]

    running_sum = numbers.pop(0)
    while numbers:
        running_sum = [running_sum, numbers.pop(0)]
        reduction(running_sum)

    return get_magnitude(running_sum)


for i, v in sample_lines.items():
    print(f"Sample output {i}:", process(v))
print("Answer:", process(input_lines))

# pypy ./day_18/part_1.py
