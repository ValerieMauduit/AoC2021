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

# Second star: Now, discard the corrupted lines. The remaining lines are incomplete. Incomplete lines don't have any
# incorrect characters - instead, they're missing some closing characters at the end of the line. To repair the
# navigation subsystem, you just need to figure out the sequence of closing characters that complete all open chunks in
# the line.
# Did you know that autocomplete tools also have contests? It's true! The score is determined by considering the
# completion string character-by-character. Start with a total score of 0. Then, for each character, multiply the total
# score by 5 and then increase the total score by the point value given for the character in the following table:
# - ): 1 point.
# - ]: 2 points.
# - }: 3 points.
# - >: 4 points.
# Autocomplete tools are an odd bunch: the winner is found by sorting all the scores and then taking the middle score.
# (There will always be an odd number of scores to consider.) Find the completion string for each incomplete line, score
# the completion strings, and sort the scores. What is the middle score?

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from numpy import median
from AoC_tools.read_data import read_data


CORRESPONDING = {'(': ')', '[': ']', '{': '}', '<': '>'}
CORRUPTION_SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137} # 3, 3 * 19, 3 * 19 * 21, 3 * 19 * 21 * 21
COMPLETION_SCORES = {')': 1, ']': 2, '}': 3, '>': 4}


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


def corruption_score(characters):
    return sum([CORRUPTION_SCORES[character] for character in characters])


def find_incomplete_lines(data):
    return [line for line in data if line not in [corrupted['line'] for corrupted in find_corrupted_lines(data)]]


def complete_line(line, completion=''):
    if line == '':
        return completion
    elif line[0] in ['(', '<', '[', '{']:
        return complete_line(line[1:], CORRESPONDING[line[0]] + completion)
    elif line[0] == completion[0]:
        return complete_line(line[1:], completion[1:])
    else:
        raise Exception(f"Unexpected set of data, line: '{line}' with closing set '{completion}'")


def complete_lines(data):
    incomplete_lines = find_incomplete_lines(data)
    additions = [complete_line(line) for line in incomplete_lines]
    return additions


def completion_score(additions):
    scores = []
    for addition in additions:
        line_score = 0
        for character in addition:
            line_score = line_score * 5 + COMPLETION_SCORES[character]
        scores += [line_score]
    return int(median(scores))


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day10.txt', numbers=False)

    if star == 1:  # The final answer is: 311895
        solution = corruption_score([corrupted['character'] for corrupted in find_corrupted_lines(data)])
    elif star == 2:  # The final answer is: 2904180541
        solution = completion_score(complete_lines(data))
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
