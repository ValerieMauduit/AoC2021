# Day 05: Hydrothermal Venture

# First star: You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large,
# opaque clouds, so it would be best to avoid them if possible. They tend to form in lines; the submarine helpfully
# produces a list of nearby lines of vents (your puzzle input) for you to review. Each line of vents is given as a line
# segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the
# coordinates of the other end. These line segments include the points at both ends.
# To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap.
# Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

# Second star: Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need
# to also consider diagonal lines. Because of the limits of the hydrothermal vent mapping system, the lines in your list
# will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees.
# You still need to determine the number of points where at least two lines overlap. Consider all of the lines. At how
# many points do at least two lines overlap?

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import re
import itertools
import numpy as np

from AoC_tools.read_data import read_data
from AoC_tools.work_with_maps import AocMap


def create_map(data, include_diagonals=False):
    clouds = [[int(x) for x in re.split(' -> |,', cloud)] for cloud in data]
    all_clouds_coordinates = [[[cloud[0], cloud[1]], [cloud[2], cloud[3]]] for cloud in clouds]
    hv_clouds = []
    diag_clouds = []
    for cloud in all_clouds_coordinates:
        if (cloud[0][0] == cloud[1][0]) | (cloud[0][1] == cloud[1][1]):
            hv_clouds += [cloud]
        elif include_diagonals:
            diag_clouds += [cloud]
    coordinates = list(itertools.chain(*(hv_clouds + diag_clouds)))
    x_min = min([coord[0] for coord in coordinates])
    y_min = min([coord[1] for coord in coordinates])
    clouds_map = AocMap.empty_from_size(
        max([coord[0] for coord in coordinates]) - x_min + 1,
        max([coord[1] for coord in coordinates]) - y_min + 1
    )
    clouds_map.origin = [x_min, y_min]
    for cloud in hv_clouds:
        x_min = min([cloud[0][0], cloud[1][0]])
        x_max = max([cloud[0][0], cloud[1][0]])
        y_min = min([cloud[0][1], cloud[1][1]])
        y_max = max([cloud[0][1], cloud[1][1]])
        for point in [[x, y] for x in range(x_min, x_max + 1) for y in range(y_min, y_max + 1)]:
            if clouds_map.get_point(point) == '.':
                clouds_map.set_point(point, 1)
            else:
                clouds_map.set_point(point, clouds_map.get_point(point) + 1)
    for cloud in diag_clouds:
        dx, dy = np.sign(cloud[1][0] - cloud[0][0]), np.sign(cloud[1][1] - cloud[0][1])
        x, y = cloud[0][0] - dx, cloud[0][1] - dy
        while x != cloud[1][0]:
            x += dx
            y += dy
            point = [x, y]
            if clouds_map.get_point(point) == '.':
                clouds_map.set_point(point, 1)
            else:
                clouds_map.set_point(point, clouds_map.get_point(point) + 1)
    return clouds_map


def count_overlaps(clouds_map):
    return sum([x > 1 for line in clouds_map for x in line if x != '.'])


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day05.txt', numbers=False)

    if star == 1:  # The final answer is: 7414
        solution = count_overlaps(create_map(data).map)
    elif star == 2:  # The final answer is: 19676
        solution = count_overlaps(create_map(data, True).map)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
