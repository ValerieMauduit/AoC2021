# Day 10: Syntax Scoring

# First star: The navigation subsystem syntax is made of several lines containing chunks. There are one or more chunks
# on each line, and chunks contain zero or more other chunks. Adjacent chunks are not separated by any delimiter; if one
# chunk stops, the next chunk (if any) can immediately start. Every chunk must open and close with one of four legal
# pairs of matching characters:
# - If a chunk opens with (, it must close with ).
# - If a chunk opens with [, it must close with ].
# - If a chunk opens with {, it must close with }.
# - If a chunk opens with <, it must close with >.
# Some lines are incomplete, but others are corrupted. Find and discard the corrupted lines first. A corrupted line is
# one where a chunk closes with the wrong character - that is, where the characters it opens and closes with do not form
# one of the four legal pairs listed above. Stop at the first incorrect closing character on each corrupted line.
# Did you know that syntax checkers actually have contests to see who can get the high score for syntax errors in a
# file? It's true! To calculate the syntax error score for a line, take the first illegal character on the line and
# look it up in the following table:
# - ): 3 points.
# - ]: 57 points.
# - }: 1197 points.
# - >: 25137 points.
# Find the first illegal character in each corrupted line of the navigation subsystem. What is the total syntax error
# score for those errors?

# Second star: description

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data


CORRESPONDING = {'(': ')', '[': ']', '{': '}', '<': '>'}
SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137} # 3, 3 * 19, 3 * 19 * 21, 3 * 19 * 21 * 21


def find_corrupted_lines(data):
    corrupted_lines = []
    for line in data:
        corruption_check = corruption(line)
        if corruption_check['corrupted']:
            corrupted_lines += [{'line': line, 'character': corruption_check['character']}]
    return corrupted_lines


def corruption(line, expected=None):
    if expected is None:
        expected = []
    if line == '':
        return {'corrupted': False}
    else:
        if line[0] in ['(', '<', '[', '{']:
            return corruption(line[1:], [CORRESPONDING[line[0]]] + expected)
        elif len(expected) == 0:
            return {'corrupted': True, 'character': line[0]}
        elif line[0] == expected[0]:
            return corruption(line[1:], expected[1:])
        else:
            return {'corrupted': True, 'character': line[0]}


def score(characters):
    return sum([SCORES[character] for character in characters])


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day10.txt', numbers=False)

    if star == 1:  # The final answer is: 311895
        solution = score([corrupted['character'] for corrupted in find_corrupted_lines(data)])
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
