# Day 11: Dumbo Octopus

# First star: There are 100 octopuses arranged neatly in a 10 by 10 grid. Each octopus slowly gains energy over time and
# flashes brightly for a moment when its energy is full. Each octopus has an energy level - your submarine can remotely
# measure the energy level of each octopus (your puzzle input). The energy level of each octopus is a value between 0
# and 9. You can model the energy levels and flashes of light in steps. During a single step, the following occurs:
# - First, the energy level of each octopus increases by 1.
# - Then, any octopus with an energy level greater than 9 flashes. This increases the energy level of all adjacent
#   octopuses by 1, including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level
#   greater than 9, it also flashes. This process continues as long as new octopuses keep having their energy level
#   increased beyond 9. (An octopus can only flash at most once per step.)
# - Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to
#   flash.
# Given the starting energy levels of the dumbo octopuses in your cavern, simulate 100 steps. How many total flashes are
# there after 100 steps?

# Second star: If you can calculate the exact moments when the octopuses will all flash simultaneously, you should be
# able to navigate through the cavern. What is the first step during which all octopuses flash?

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data
from AoC_tools.work_with_maps import AocMap


def run_steps(data, steps=100):
    octopus_map = AocMap(data, numbers=True)
    flashes = 0
    for step in range(steps):
        # All octopuses increase by 1
        octopus_map.apply_function(lambda x: x + 1)
        # Octopuses flash
        changes = True
        while changes is True:
            changes = False
            for y in range(octopus_map.height):
                for x in range(octopus_map.width):
                    if octopus_map.get_point([x, y]) > 9:
                        octopus_map.set_position([x, y])
                        flashes += 1
                        changes = True
                        for neighbour in octopus_map.get_neighbours_coordinates():
                            if octopus_map.get_point(neighbour) > 0:
                                octopus_map.set_point(neighbour, octopus_map.get_point(neighbour) + 1)
                        octopus_map.set_point([x, y], -1)
        # After flashes, they all go back to 0
        octopus_map.change_marker(-1, 0)
    return {'map': octopus_map.map, 'flashes': flashes}


def run_until_synchronization(data):
    octopus_map = AocMap(data, numbers=True)
    steps = 0
    flashes = 0
    while flashes < octopus_map.height * octopus_map.width:
        steps += 1
        # All octopuses increase by 1
        octopus_map.apply_function(lambda x: x + 1)
        # Octopuses flash
        changes = True
        while changes is True:
            changes = False
            for y in range(octopus_map.height):
                for x in range(octopus_map.width):
                    if octopus_map.get_point([x, y]) > 9:
                        octopus_map.set_position([x, y])
                        flashes += 1
                        changes = True
                        for neighbour in octopus_map.get_neighbours_coordinates():
                            if octopus_map.get_point(neighbour) > 0:
                                octopus_map.set_point(neighbour, octopus_map.get_point(neighbour) + 1)
                        octopus_map.set_point([x, y], -1)
        # After flashes, they all go back to 0
        octopus_map.change_marker(-1, 0)
        # Count flashes at this step
        flashes = octopus_map.count_marker(0)
    return steps


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day11.txt', numbers=False)

    if star == 1:  # The final answer is: 1694
        solution = run_steps(data)
    elif star == 2:  # The final answer is: 346
        solution = run_until_synchronization(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
