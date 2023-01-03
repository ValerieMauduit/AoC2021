# Day 03: Binary Diagnostic

# First star: The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded
# properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the
# power consumption.
# You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate
# and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.
# Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all
# numbers in the diagnostic report. The epsilon rate is calculated in a similar way; rather than use the most common
# bit, the least common bit from each position is used.
# Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them
# together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)

# Second star: Next, you should verify the life support rating, which can be determined by multiplying the oxygen
# generator rating by the CO2 scrubber rating. Both the oxygen generator rating and the CO2 scrubber rating are values
# that can be found in your diagnostic report - finding them is the tricky part. Both values are located using a similar
# process that involves filtering out values until only one remains. Before searching for either rating value, start
# with the full list of binary numbers from your diagnostic report and consider just the first bit of those numbers.
# Then:
# - Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard
#   numbers which do not match the bit criteria.
# - If you only have one number left, stop; this is the rating value for which you are searching.
# - Otherwise, repeat the process, considering the next bit to the right.
# The bit criteria depends on which type of rating value you want to find:
# - To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only
#   numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being
#   considered.
# - To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only
#   numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being
#   considered.

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data

import numpy as np


def most_common_bit(data, column):
    values = [int(line[column]) for line in data]
    return 1 - int(np.round(1 - np.mean(values)))


def gamma_epsilon(data, column):
    most_common = most_common_bit(data, column)
    return {'gamma': str(most_common), 'epsilon': str(1 - most_common)}


def binary_oxygen_rate(data):
    column = 0
    while len(data) > 1:
        bit = most_common_bit(data, column)
        data = [line for line in data if int(line[column]) == bit]
        column += 1
    return data[0]


def binary_co2_rate(data):
    column = 0
    while len(data) > 1:
        bit = 1 - most_common_bit(data, column)
        data = [line for line in data if int(line[column]) == bit]
        column += 1
    return data[0]


def binary_power_consumption(data):
    rates = {'gamma': '', 'epsilon': ''}
    for column in range(len(data[0])):
        values = gamma_epsilon(data, column)
        rates['gamma'] += values['gamma']
        rates['epsilon'] += values['epsilon']
    return rates


def get_score(rates):
    score = 1
    for key in rates:
        score *= int(rates[key], 2)
    return score


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day03.txt', numbers=False)

    if star == 1:  # The final answer is: 3429254
        solution = get_score(binary_power_consumption(data))
    elif star == 2:  # The final answer is: 5410338
        solution = get_score({'oxygen': binary_oxygen_rate(data), 'co2': binary_co2_rate(data)})
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
