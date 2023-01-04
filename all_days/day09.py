# Day 09: Smoke Basin

# First star: The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input). Smoke
# flows to the lowest point of the area it's in. Each number corresponds to the height of a particular location, where 9
# is the highest and 0 is the lowest a location can be.
# Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most
# locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have
# three or two adjacent locations, respectively. The risk level of a low point is 1 plus its height. Find all of the low
# points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

# Second star: description

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data
from AoC_tools.work_with_maps import AocMap


def risk_level(points):
    return sum(points) + len(points)


def get_low_points(data):
    heightmap = AocMap(data, numbers=True)
    low_points = []
    for y in range(heightmap.height):
        for x in range(heightmap.width):
            heightmap.set_position([x, y])
            if heightmap.get_point([x, y]) < min(heightmap.get_neighbours(False)):
                low_points += [heightmap.get_point([x, y])]
    return low_points


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day09.txt', numbers=False)

    if star == 1:  # The final answer is: 436
        solution = risk_level(get_low_points(data))
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
