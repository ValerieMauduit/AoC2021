# Day 15: Chiton

# First star: The cavern is large, but has a very low ceiling, restricting your motion to two dimensions. The shape of
# the cavern resembles a square; a quick scan of chiton density produces a map of risk level throughout the cave (your
# puzzle input). You start in the top left position, your destination is the bottom right position, and you cannot move
# diagonally. The number at each position is its risk level; to determine the total risk of an entire path, add up the
# risk levels of each position you enter. Your goal is to find a path with the lowest total risk.
# What is the lowest total risk of any path from the top left to the bottom right?

# Second star: description

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data
from AoC_tools.work_with_maps import AocMap


def best_path_risk(chiton_map):
    risk_map = AocMap.empty_from_size(chiton_map.width, chiton_map.height)
    risk_map.set_point([0, 0], 0)
    for x in range(risk_map.width):
        for y in range(risk_map.height):
            risk_map.set_position([x, y])
            filled_neighbours = [v for v in risk_map.get_neighbours(False) if v != '.']
            if len(filled_neighbours) > 0:
                previous_value = risk_map.get_point([x, y])
                if type(previous_value) == str:
                    previous_value = 100 * risk_map.height * risk_map.width
                new_value = (chiton_map.get_point([x, y]) + min(filled_neighbours))
                if new_value < previous_value:
                    risk_map.set_point([x, y], new_value)
    print(risk_map.get_point([risk_map.width - 1, risk_map.height - 1]))
    return risk_map.get_point([risk_map.width - 1, risk_map.height - 1])


def tile_translation(x, n):
    if x + n < 10:
        return x + n
    else:
        return x + n - 9


def best_path_risk_in_five_times_larger(data):
    chiton_map = AocMap(data, numbers=True)
    origin_tile = chiton_map.copy()
    for x in range(1, 5):
        new_tile = origin_tile.copy()
        new_tile.apply_function(lambda v: tile_translation(v, x))
        chiton_map.glue_map(new_tile, 'R')
    origin_line = chiton_map.copy()
    for y in range(1, 5):
        new_line = origin_line.copy()
        new_line.apply_function(lambda v: tile_translation(v, y))
        chiton_map.glue_map(new_line, 'D')
    return best_path_risk(chiton_map)


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day15.txt', numbers=False)
    data = [[int(x) for x in line] for line in data]

    if star == 1:  # The final answer is: 652
        solution = best_path_risk(AocMap(data, numbers=True))
    elif star == 2:  # The final answer is: 2938
        solution = best_path_risk_in_five_times_larger(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
