# Day 09: Smoke Basin

# First star: The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input). Smoke
# flows to the lowest point of the area it's in. Each number corresponds to the height of a particular location, where 9
# is the highest and 0 is the lowest a location can be.
# Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most
# locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have
# three or two adjacent locations, respectively. The risk level of a low point is 1 plus its height. Find all of the low
# points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

# Second star: Next, you need to find the largest basins so you know what areas are most important to avoid. A basin is
# all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although
# some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will
# always be part of exactly one basin. The size of a basin is the number of locations within the basin, including the
# low point.
# What do you get if you multiply together the sizes of the three largest basins?

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
    low_points = {'coordinates': [], 'values': []}
    for y in range(heightmap.height):
        for x in range(heightmap.width):
            heightmap.set_position([x, y])
            if heightmap.get_point([x, y]) < min(heightmap.get_neighbours(False)):
                low_points['values'] += [heightmap.get_point([x, y])]
                low_points['coordinates'] += [[x, y]]
    return low_points


def get_basins_sizes(data):
    heightmap = AocMap(data, numbers=True)
    basins_map = AocMap.empty_from_size(heightmap.width, heightmap.height)
    low_points = get_low_points(data)
    count_low_points = len(low_points['coordinates'])
    basins_map.set_points(low_points['coordinates'], [x for x in range(count_low_points)])
    while basins_map.count_marker('.') > 0:
        for y in range(heightmap.height):
            for x in range(heightmap.width):
                if basins_map.get_point([x, y]) == '.':
                    if heightmap.get_point([x, y]) == 9:
                        basins_map.set_point([x, y], '#')
                    else:
                        basins_map.set_position([x, y])
                        numbered_neighbours = [x for x in basins_map.get_neighbours(False) if x not in ['.', '#']]
                        if len(numbered_neighbours) > 0:
                            basins_map.set_point([x, y], numbered_neighbours[0])
    basins_sizes = [basins_map.count_marker(x) for x in range(count_low_points)]
    return basins_sizes


def score(basins_sizes):
    basins_sizes.sort()
    basins_sizes.reverse()
    return basins_sizes[0] * basins_sizes[1] * basins_sizes[2]


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day09.txt', numbers=False)

    if star == 1:  # The final answer is: 436
        solution = risk_level(get_low_points(data)['values'])
    elif star == 2:  # The final answer is: 1317792
        solution = score(get_basins_sizes(data))
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
