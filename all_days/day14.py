# Day 14: Extended Polymerization

# First star: The submarine manual contains instructions for finding the optimal polymer formula; specifically, it
# offers a polymer template and a list of pair insertion rules (your puzzle input). You just need to work out what
# polymer would result after repeating the pair insertion process a few times. The first line is the polymer template -
# this is the starting point of the process.
# The following section defines the pair insertion rules. A rule like AB -> C means that when elements A and B are
# immediately adjacent, element C should be inserted between them. These insertions all happen simultaneously.
# Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result.
# What do you get if you take the quantity of the most common element and subtract the quantity of the least common
# element?

# Second star: description

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data
import AoC_tools.work_with_lists as aoc_lists


def insertions(template, rules, steps=1):
    polymer = template
    for step in range(steps):
        pairs = aoc_lists.sliding_windows(polymer, 2)
        inserted = [rules[pair] for pair in pairs]
        polymer = ''.join(aoc_lists.merge_lists(aoc_lists.str_to_list(polymer[:-1]), inserted)) + polymer[-1]
    return polymer


def score(polymer):
    print(polymer)
    print(aoc_lists.most_common(polymer))
    print(aoc_lists.least_common(polymer))
    return aoc_lists.most_common(polymer)[1] - aoc_lists.least_common(polymer)[1]


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day14.txt', numbers=False, by_block=True)
    polymer_template = data[0]
    insertion_rules = {rule[0]: rule[1] for rule in [[x for x in line.split(' -> ')] for line in data[1]]}

    if star == 1:  # The final answer is 2233
        solution = score(insertions(polymer_template, insertion_rules, 11))
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
