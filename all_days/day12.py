# Day 12: Passage Pathing

# First star: description

# Second star: description

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data
from AoC_tools.work_with_graphs import AocGraph


def count_paths(caves, from_node='start', to_node='end', forbidden=None):
    if forbidden is None:
        forbidden = []
    if from_node == to_node:
        return 1
    else:
        total = 0
        for neighbour in caves.get_neighbours(from_node, True):
            if neighbour not in forbidden:
                if from_node.lower() == from_node:
                    branch_forbidden = forbidden + [from_node]
                else:
                    branch_forbidden = forbidden
                total += count_paths(caves, neighbour, to_node, branch_forbidden)
        return total


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day12.txt', numbers=False, split='-')

    if star == 1:  # The final answer is: 5576
        solution = count_paths(AocGraph(data))
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
