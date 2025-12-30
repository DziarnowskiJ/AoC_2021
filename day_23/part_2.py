import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_23.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_23.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

import heapq
from itertools import count
import re

amphi_room_id = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3
}

room_amphi = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D'
}

amphi_step_costs = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

room_positions = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}


def parse(lines):
    row_0 = re.findall(r'\w', lines[2])
    row_1 = ('D', 'C', 'B', 'A')
    row_2 = ('D', 'B', 'A', 'C')
    row_3 = re.findall(r'\w', lines[3])
    rooms = tuple(zip(row_0, row_1, row_2, row_3))
    print(rooms)
    return rooms


def process(lines):
    init_rooms = parse(lines)
    init_hallway = (None,) * 11
    init_state = (init_rooms, init_hallway)

    goal = (('A', 'A', 'A', 'A'), ('B', 'B', 'B', 'B'), ('C', 'C', 'C', 'C'), ('D', 'D', 'D', 'D'))

    counter = count()
    visited = {}
    queue = [(0, next(counter), init_state)]

    while queue:
        cost, _, (rooms, hallway) = heapq.heappop(queue)

        if (rooms, hallway) in visited and visited[(rooms, hallway)] <= cost:
            continue
        visited[(rooms, hallway)] = cost

        if hallway == (None,) * 11 and rooms == goal:
            return cost

        # --- Hallway -> Room ---
        for hall_pos, amphi in enumerate(hallway):
            if amphi is None: continue

            r_idx = amphi_room_id[amphi]
            target_room = rooms[r_idx]

            # Can enter if room only contains same type or is empty
            if all(slot is None or slot == amphi for slot in target_room):
                room_pos = room_positions[amphi]
                step = 1 if room_pos > hall_pos else -1
                if all(hallway[p] is None for p in range(hall_pos + step, room_pos + step, step)):
                    # Find deepest None slot
                    slot_idx = max(idx for idx, val in enumerate(target_room) if val is None)
                    dist = abs(room_pos - hall_pos) + (slot_idx + 1)

                    new_hall = list(hallway)
                    new_hall[hall_pos] = None
                    new_rooms = [list(r) for r in rooms]
                    new_rooms[r_idx][slot_idx] = amphi

                    new_state = (tuple(tuple(r) for r in new_rooms), tuple(new_hall))
                    heapq.heappush(queue, (cost + dist * amphi_step_costs[amphi], next(counter), new_state))

        # --- Room -> Hallway ---
        for r_idx, room in enumerate(rooms):
            room_type = room_amphi[r_idx]
            if all(slot is None or slot == room_type for slot in room):
                continue  # Room is already "good"

            # Find top-most amphipod
            slot_idx, amphi = next((i, s) for i, s in enumerate(room) if s is not None)
            curr_room_x = room_positions[room_type]

            for hall_pos in [0, 1, 3, 5, 7, 9, 10]:  # Valid stop positions
                step = 1 if hall_pos > curr_room_x else -1
                if all(hallway[p] is None for p in range(curr_room_x, hall_pos + step, step)):
                    dist = (slot_idx + 1) + abs(hall_pos - curr_room_x)

                    new_hall = list(hallway)
                    new_hall[hall_pos] = amphi
                    new_rooms = [list(r) for r in rooms]
                    new_rooms[r_idx][slot_idx] = None

                    new_state = (tuple(tuple(r) for r in new_rooms), tuple(new_hall))
                    heapq.heappush(queue, (cost + dist * amphi_step_costs[amphi], next(counter), new_state))


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_23/part_1.py
