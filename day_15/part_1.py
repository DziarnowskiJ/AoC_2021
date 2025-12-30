import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_15.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_15.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]
  
from utils.geometry import *
from utils.search import dijkstra_weighted
    
def process(lines):
    grid = grid_dict(lines)
    nw, se = grid_dimensions(grid)
    path, visited = dijkstra_weighted(nw, se, grid)
    return sum([int(grid[p]) for p in path[1:]])


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_15/part_1.py

