import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_19.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_19.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

import re
from utils.geometry3D import *
from itertools import combinations
from collections import defaultdict


def parse(lines):
    scanners = dict()
    is_first = True
    scanner_id = None
    for line in lines:
        if is_first:
            scanner_id = int(re.findall(r'\d+', line)[0])
            scanners[scanner_id] = []
            is_first = False
        elif line == '':
            is_first = True
            scanner_id = None
        else:
            scanners[scanner_id].append(Point(*[int(p) for p in re.findall(r'-?\d+', line)]))

    return scanners


def get_rotations(p: Point):
    x, y, z = p.x, p.y, p.z
    return {i: rot for i, rot in enumerate([
        Point(x, y, z),
        Point(x, -z, y),
        Point(x, -y, -z),
        Point(x, z, -y),
        Point(-x, -y, z),
        Point(-x, -z, -y),
        Point(-x, y, -z),
        Point(-x, z, y),
        Point(y, z, x),
        Point(y, -x, z),
        Point(y, -z, -x),
        Point(y, x, -z),
        Point(-y, -z, x),
        Point(-y, -x, -z),
        Point(-y, z, -x),
        Point(-y, x, z),
        Point(z, x, y),
        Point(z, -y, x),
        Point(z, -x, -y),
        Point(z, y, -x),
        Point(-z, -x, y),
        Point(-z, -y, -x),
        Point(-z, x, -y),
        Point(-z, y, x)])}


def adjust_scanner(scanner1: list[Point], p1: Point, scanner2: list[Point], p2: Point):
    scanner2_rotations = defaultdict(list)
    scanner2_ = {p: get_rotations(p) for p in scanner2}
    for p, p_d in scanner2_.items():
        for rot, p_rot in p_d.items():
            scanner2_rotations[rot].append(p_rot)

    scanner1_set = set(scanner1)

    for rot_idx, point in get_rotations(p2).items():
        offset = p1 - point
        offset_points = {off_point + offset for off_point in scanner2_rotations[rot_idx]}
        if len(scanner1_set & offset_points) >= 12:
            # Adjusted points, rotation, adjusted beacon
            return offset_points, rot_idx, offset


def get_distances(scanner: list[Point]):
    return {straight_distance(x, y): (x, y) for x, y in combinations(scanner, 2)}


def process(lines):
    scanners = parse(lines)
    scanners_edges = {s: get_distances(ps) for s, ps in scanners.items()}

    full_scan = set(scanners[0])
    all_beacons = {Point(0, 0, 0)}

    queue = [(0, scanners[0])]

    unfixed_ids = set(scanners.keys())
    unfixed_ids.remove(0)

    while queue:
        ref_id, ref_points = queue.pop(0)
        ref_edges = get_distances(ref_points)

        found_this_round = []
        for unfixed_id in unfixed_ids:
            common_distances = ref_edges.keys() & scanners_edges[unfixed_id].keys()

            if len(common_distances) >= 66:
                common_edge = list(common_distances)[0]
                ps_ref = ref_edges[common_edge]
                ps_new = scanners_edges[unfixed_id][common_edge]

                res = adjust_scanner(list(ref_points), ps_ref[0], scanners[unfixed_id], ps_new[0])
                if not res:
                    res = adjust_scanner(list(ref_points), ps_ref[0], scanners[unfixed_id], ps_new[1])

                if res:
                    offset_points, rot_idx, offset = res

                    full_scan.update(offset_points)
                    all_beacons.add(offset)

                    queue.append((unfixed_id, list(offset_points)))
                    found_this_round.append(unfixed_id)
        for fid in found_this_round:
            unfixed_ids.remove(fid)

    return max([distance(*pair) for pair in combinations(all_beacons, 2)])


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./day_19/part_1.py
