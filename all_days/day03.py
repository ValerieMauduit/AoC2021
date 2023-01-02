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

# Second star: description

import numpy as np


def gamma_epsilon(data, column):
    values = [int(line[column]) for line in data]
    if np.mean(values) < 0.5:
        return {'gamma': '0', 'epsilon': '1'}
    else:
        return {'gamma': '1', 'epsilon': '0'}


def binary_power_consumption(data):
    rates = {'gamma': '', 'epsilon': ''}
    for column in range(len(data[0])):
        values = gamma_epsilon(data, column)
        rates['gamma'] += values['gamma']
        rates['epsilon'] += values['epsilon']
    return rates


def score(data):
    rates = binary_power_consumption(data)
    return int(rates['gamma'], 2) * int(rates['epsilon'], 2)


def run(data_dir, star):
    with open(f'{data_dir}/input-day03.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 3429254
        solution = score(data)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
