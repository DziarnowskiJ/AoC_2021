import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_9.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_9.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]
  
from utils.geometry import *
  
    
def process(lines):
    grid = grid_dict(lines)
    resp = 0
    for point, val in grid.items():
        if int(val) < min([int(i) for i in get_neighbours_values(point, grid)]):
            resp += int(val) + 1
    return resp

print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_09/part_1.py

