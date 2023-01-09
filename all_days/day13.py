# Day 13: Transparent Origami

# First star: To your surprise, you manage to find the manual; as you go to open it, page 1 falls out. It's a large
# sheet of transparent paper! The transparent paper is marked with random dots and includes instructions on how to fold
# it up (your puzzle input). The first section is a list of dots on the transparent paper. 0,0 represents the top-left
# coordinate. The first value, x, increases to the right. The second value, y, increases downward. Then, there is a list
# of fold instructions. Each instruction indicates a line on the transparent paper and wants you to fold the paper up
# (for horizontal y=... lines) or left (for vertical x=... lines). How many dots are visible after completing just the
# first fold instruction on your transparent paper?

# Second star: Finish folding the transparent paper according to the instructions. The manual says the code is always
# eight capital letters. What code do you use to activate the infrared thermal imaging camera system?

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data
from AoC_tools.work_with_maps import AocMap


def fold_map(coordinates, folds):
    paper = AocMap.from_coord(coordinates)
    for fold in folds:
        instruction = fold.split('=')
        axis, value = instruction[0][-1], int(instruction[1])
        if axis == 'x':
            superposed = paper.create_submap(x_min=value)
            superposed.reverse(vertical=True, horizontal=False)
            superposed.remove_columns(1, left=False)
            paper = paper.create_submap(x_max=value)
            paper.remove_columns(1, left=False)
            paper.superpose(superposed)
        elif axis == 'y':
            superposed = paper.create_submap(y_min=value)
            superposed.reverse(vertical=False, horizontal=True)
            superposed.remove_lines(1, top=False)
            paper = paper.create_submap(y_max=value)
            paper.remove_lines(1, top=False)
            paper.superpose(superposed)
    return paper


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day13.txt', numbers=False, by_block=True)
    coordinates = [[int(x) for x in line.split(',')] for line in data[0]]
    folds = data[1]

    if star == 1:  # The final answer is: 647
        folded_map = fold_map(coordinates, [folds[0]])
        solution = folded_map.count_marker('#')
    elif star == 2:  # The final answer is:
        folded_map = fold_map(coordinates, folds)
        folded_map.display()
        solution = folded_map.count_marker('#')
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
