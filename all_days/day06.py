# Day 06: Lanternfish

# First star: Although you know nothing about this specific species of lanternfish, you make some guesses about their
# attributes. Surely, each lanternfish creates a new lanternfish once every 7 days.
# A lanternfish that creates a new fish resets its timer to 6, not 7 (because 0 is included as a valid timer value). The
# new lanternfish starts with an internal timer of 8 and does not start counting down until the next day.
# Realizing what you're trying to do, the submarine automatically produces a list of the ages of several hundred nearby
# lanternfish (your puzzle input).
# Find a way to simulate lanternfish. How many lanternfish would there be after 80 days?

# Second star: description

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data


def initial_fishes(data):
    fishes = {x: 0 for x in range(9)}
    for fish in data:
        fishes[fish] += 1
    return fishes


def simulate_one_day(fishes):
    new_fishes = {x: 0 for x in range(9)}
    for timer in range(1, 9):
        new_fishes[timer - 1] = fishes[timer]
    new_fishes[6] += fishes[0]
    new_fishes[8] += fishes[0]
    return new_fishes


def simulate_process(fishes, total=80):
    for n in range(total):
        fishes = simulate_one_day(fishes)
    return fishes


def count_fishes(fishes):
    return sum(fishes.values())


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day06.txt', numbers=True, split=',')[0]

    if star == 1:  # The final answer is: 396210
        solution = count_fishes(simulate_process(initial_fishes(data), 80))
    elif star == 2:  # The final answer is:
        solution = count_fishes(simulate_process(initial_fishes(data), 256))
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
