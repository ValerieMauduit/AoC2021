# Day 18: Snailfish

# First star: Snailfish numbers aren't like regular numbers. Instead, every snailfish number is a pair - an ordered list
# of two elements. Each element of the pair can be either a regular number or another pair.
# This snailfish homework is about addition. To add two snailfish numbers, form a pair from the left and right
# parameters of the addition operator. There's only one problem: snailfish numbers must always be reduced. To reduce a
# snailfish number, you must repeatedly do the first action in this list that applies to the snailfish number:
# - If any pair is nested inside four pairs, the leftmost such pair explodes.
# - If any regular number is 10 or greater, the leftmost such regular number splits.
# Once no action in the above list applies, the snailfish number is reduced.
# During reduction, at most one action applies, after which the process returns to the top of the list of actions. For
# example, if split produces a pair that meets the explode criteria, that pair explodes before other splits occur.
# To explode a pair, the pair's left value is added to the first regular number to the left of the exploding pair
# (if any), and the pair's right value is added to the first regular number to the right of the exploding pair (if any).
# Exploding pairs will always consist of two regular numbers. Then, the entire exploding pair is replaced with the
# regular number 0.
# To split a regular number, replace it with a pair; the left element of the pair should be the regular number divided
# by two and rounded down, while the right element of the pair should be the regular number divided by two and rounded
# up.
# The homework assignment involves adding up a list of snailfish numbers (your puzzle input).
# To check whether it's the right answer, the snailfish teacher only checks the magnitude of the final sum. The
# magnitude of a pair is 3 times the magnitude of its left element plus 2 times the magnitude of its right element.
# The magnitude of a regular number is just that number. Magnitude calculations are recursive.
# Add up all the snailfish numbers from the homework assignment in the order they appear. What is the magnitude of
# the final sum?

# Second star: description

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from numpy import ceil, floor
from AoC_tools.read_data import read_data


class SnailfishNumber:
    def __init__(self, text_input):
        self.regular = []
        self.altitudes = []
        altitude = 0
        for x in text_input:
            if x == '[':
                altitude += 1
            elif x == ']':
                altitude -= 1
            elif x not in [',', ' ']:
                self.regular += [int(x)]
                self.altitudes += [altitude]

    def reduce_number(self):
        while (5 in self.altitudes) | (max(self.regular) > 9):
            if 5 in self.altitudes:
                explode_position = self.altitudes.index(5)
                self.explode(explode_position)
            else:
                split_position = [x > 9 for x in self.regular].index(True)
                self.split(split_position)

    def explode(self, position):
        if position == 0:
            before = []
        else:
            before = self.regular[:(position - 1)] + [sum(self.regular[(position - 1):(position + 1)])]
        if position == len(self.regular) - 2:
            after = []
        else:
            after = [sum(self.regular[(position + 1):(position + 3)])] + self.regular[(position + 3):]
        self.regular = before + [0] + after
        self.altitudes = self.altitudes[:position] + [4] + self.altitudes[(position + 2):]

    def split(self, position):
        self.altitudes = self.altitudes[:position] + [self.altitudes[position] + 1] * 2 + self.altitudes[(position + 1):]
        values = [floor(self.regular[position] / 2), ceil(self.regular[position] / 2)]
        self.regular = self.regular[:position] + values + self.regular[(position + 1):]

    def magnitude(self):
        magnitude = self.regular
        altitudes = self.altitudes
        while len(magnitude) > 1:
            highest = max(altitudes)
            pos = altitudes.index(highest)
            magnitude = magnitude[:pos] + [magnitude[pos] * 3 + magnitude[pos + 1] * 2] + magnitude[(pos + 2):]
            altitudes = altitudes[:pos] + [highest - 1] + altitudes[(pos + 2):]
        return magnitude[0]

    def add(self, right, reduce=True):
        result = SnailfishNumber('')
        result.regular = self.regular + right.regular
        result.altitudes = [n + 1 for n in (self.altitudes + right.altitudes)]
        result.reduce_number()
        return result

    def equals(self, comparison):
        return (self.regular == comparison.regular) & (self.altitudes == comparison.altitudes)


def snailfish_addition(data):
    result = SnailfishNumber(data[0])
    result.reduce_number()
    for description in data[1:]:
        right_side = SnailfishNumber(description)
        right_side.reduce_number()
        result = result.add(right_side)
    return result


    elif star == 2:  # The final answer is:
        solution = my_func(data)
def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day18.txt', numbers=False)
    if star == 1:  # The final answer is: 3981
        solution = snailfish_addition(data).magnitude()
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
