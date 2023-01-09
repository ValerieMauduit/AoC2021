# Day 12: Passage Pathing

# First star: Fortunately, the sensors are still mostly working, and so you build a rough map of the remaining caves
# (your puzzle input). This is a list of how all of the caves are connected. You start in the cave named start, and your
# destination is the cave named end.
# Your goal is to find the number of distinct paths that start at start, end at end, and don't visit small caves more
# than once. There are two types of caves: big caves (written in uppercase, like A) and small caves (written in
# lowercase, like b). It would be a waste of time to visit any small cave more than once, but big caves are large enough
# that it might be worth visiting them multiple times. So, all paths you find should visit small caves at most once, and
# can visit big caves any number of times. How many paths through this cave system are there that visit small caves at
# most once?

# Second star: After reviewing the available paths, you realize you might have time to visit a single small cave twice.
# Specifically, big caves can be visited any number of times, a single small cave can be visited at most twice, and the
# remaining small caves can be visited at most once. However, the caves named start and end can only be visited exactly
# once each: once you leave the start cave, you may not return to it, and once you reach the end cave, the path must end
# immediately.

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data
from AoC_tools.work_with_graphs import AocGraph, next_paths


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


def all_paths_twice(graph, from_node, to_node):
    in_progress = [{'path': [from_node], 'forbidden': ['start']}]
    paths = []
    while len(in_progress) > 0:
        from_node = in_progress[0]['path'][-1]
        if from_node == to_node:
            paths += [in_progress[0]['path']]
            in_progress = in_progress[1:]
        else:
            small_caves = [cave for cave in in_progress[0]['path'] if cave.lower() == cave]
            if (from_node.lower() == from_node) & (len(small_caves) != len(set(small_caves))):
                forbidden = small_caves
            else:
                forbidden = in_progress[0]['forbidden']
            in_progress = next_paths({'path': in_progress[0]['path'], 'forbidden': forbidden}, graph) + in_progress[1:]
    return paths


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day12.txt', numbers=False, split='-')

    if star == 1:  # The final answer is: 5576
        solution = count_paths(AocGraph(data))
    elif star == 2:  # The final answer is: 152837
        solution = len(all_paths_twice(AocGraph(data), 'start', 'end'))
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
