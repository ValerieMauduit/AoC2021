# Day 08: Seven Segment Search

# First star: Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a
# through g:
#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg
# So, to render a 1, only segments c and f would be turned on; the rest would be off. To render a 7, only segments a, c,
# and f would be turned on. The problem is that the signals which control the segments have been mixed up on each
# display. The submarine is still trying to display numbers by producing output on signal wires a through g, but those
# wires are connected to segments randomly. Worse, the wire/segment connections are mixed up separately for each
# four-digit display! (All of the digits within a display use the same connections, though.) For each display, you watch
# the changing signals for a while, make a note of all ten unique signal patterns you see, and then write down a single
# four digit output value (your puzzle input). Using the signal patterns, you should be able to work out which pattern
# corresponds to which digit. Each entry consists of ten unique signal patterns, a | delimiter, and finally the four
# digit output value. Within an entry, the same wire/segment connections are used (but you don't know what the
# connections actually are). The unique signal patterns correspond to the ten different ways the submarine tries to
# render a digit using the current wire/segment connections. Because the digits 1, 4, 7, and 8 each use a unique number
# of segments, you should be able to tell which combinations of signals correspond to those digits.
# In the output values, how many times do digits 1, 4, 7, or 8 appear?


# Second star: For each entry, determine all of the wire/segment connections and decode the four-digit output values.
# What do you get if you add up all of the output values?

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data


def count_unique(data):
    count = 0
    for line in data:
        print(line[1])
        outputs = line[1].split(' ')
        for digit in outputs:
            if len(digit) in [2, 3, 4, 7]:
                count += 1
    return count


def count_on_left(letter, left):
    return sum([letter in digit for digit in left])


def get_output_numbers(data):
    numbers = []
    for line in data:
        inputs = line[0].split(' ')
        outputs = line[1].split(' ')
        number = ''
        for output in outputs:
            size = len(output)
            if size == 2:
                number += '1'
            elif size == 3:
                number += '7'
            elif size == 4:
                number += '4'
            elif size == 5:
                analysis = {}
                for letter in output:
                    analysis[letter] = count_on_left(letter, inputs)
                if 4 in analysis.values():
                    number += '2'
                elif 6 in analysis.values():
                    number += '5'
                else:
                    number += '3'
            elif size == 6:
                analysis = {}
                for letter in output:
                    analysis[letter] = count_on_left(letter, inputs)
                if sum([x == 7 for x in analysis.values()]) == 1:
                    number += '0'
                elif 4 not in analysis.values():
                    number += '9'
                else:
                    number += '6'
            elif size == 7:
                number += '8'
            else:
                raise Exception(f'This size is abnormal, are you sure of the digit {output}?')
        numbers += [int(number)]
    return numbers


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day08.txt', numbers=False, split=' | ')

    if star == 1:  # The final answer is: 543
        solution = count_unique(data)
    elif star == 2:  # The final answer is:
        solution = sum(get_output_numbers(data))
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
