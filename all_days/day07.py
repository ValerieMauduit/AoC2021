# Day 07: The Treachery of Whales

# First star: You quickly make a list of the horizontal position of each crab (your puzzle input). Crab submarines have
# limited fuel, so you need to find a way to make all of their horizontal positions match while requiring them to spend
# as little fuel as possible. Each change of 1 step in horizontal position of a single crab costs 1 fuel. Determine the
# horizontal position that the crabs can align to using the least fuel possible. How much fuel must they spend to align
# to that position?

# Second star: description

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data


def fuel_spent(data, position):
    return sum([abs(x - position) for x in data])


def minimum_fuel(data):
    fuel = len(data) * (max(data) - min(data))
    for position in range(min(data), max(data) + 1):
        fuel = min([fuel_spent(data, position), fuel])
    return fuel


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day07.txt', numbers=True, split=',')[0]

    if star == 1:  # The final answer is: 347509
        solution = minimum_fuel(data)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
