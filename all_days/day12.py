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


# TODO: why do I allow to visit twice all the little cave?
def paths_visit_twice(
        caves, from_node='start', to_node='end', visited_small_caves=None, allow_two_visits=True,
        forbidden_caves=None, path=None
):
    if path is None:
        path = []
    if visited_small_caves is None:
        visited_small_caves = []
    if forbidden_caves is None:
        forbidden_caves = ['start']
    if from_node == to_node:
        path += [to_node]
        return [path]
    else:
        paths = []
        if from_node.lower() == from_node:
            if allow_two_visits & (from_node in visited_small_caves):
                allow_two_visits = False
                forbidden_in_branch = forbidden_caves + visited_small_caves + [from_node]
            else:
                allow_two_visits = True
                forbidden_in_branch = forbidden_caves
            visited_in_branch = visited_small_caves + [from_node]
        else:
            forbidden_in_branch = forbidden_caves
            visited_in_branch = visited_small_caves
        for neighbour in [cave for cave in caves.get_neighbours(from_node, True) if cave not in forbidden_caves]:
            paths += paths_visit_twice(
                caves, neighbour, to_node, visited_in_branch, allow_two_visits,
                forbidden_in_branch, path + [from_node]
            )
        return paths


def count_paths_visit_twice(caves):
    too_many_paths = paths_visit_twice(caves)
    count = 0
    small_caves = [cave for cave in caves.nodes if cave.lower() == cave]
    for path in too_many_paths:
        doubles = 0
        for cave in small_caves:
            if sum([node == cave for node in path]) > 1:
                doubles += 1
        if doubles < 2:
            count += 1
    return count


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day12.txt', numbers=False, split='-')

    if star == 1:  # The final answer is: 5576
        solution = count_paths(AocGraph(data))
    elif star == 2:  # The final answer is:
        solution = count_paths_visit_twice(AocGraph(data))
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
