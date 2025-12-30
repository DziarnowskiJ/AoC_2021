import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_3.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_3.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

from utils.lists import transpose


def swap(x):
    # Swap 0 to 1 and 1 to 0
    return str(abs(int(x) - 1))


def process(lines):
    search_lines = lines.copy()

    m_bits = transpose([[l for l in line] for line in search_lines])
    for p in range(len(lines[0])):
        most_common = max(m_bits[p], key=lambda x: (m_bits[p].count(x), int(x)))
        m_bits = transpose([bit for bit in transpose(m_bits) if bit[p] == most_common])

    l_bits = transpose([[l for l in line] for line in search_lines])
    for p in range(len(lines[0])):
        least_common = min(l_bits[p], key=lambda x: (l_bits[p].count(x), int(x)))
        l_bits = transpose([bit for bit in transpose(l_bits) if bit[p] == least_common])

    return int(''.join(transpose(m_bits)[0]), 2) * int(''.join(transpose(l_bits)[0]), 2)

print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_03/part_1.py
