# Day 01: Sonar Sweep

# First star: As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the
# nearby sea floor. On a small screen, the sonar sweep report (your puzzle input) appears: each line is a measurement of
# the sea floor depth as the sweep looks further and further away from the submarine.
# The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing
# with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.
# To do this, count the number of times a depth measurement increases from the previous measurement. (There is no
# measurement before the first measurement.) How many measurements are larger than the previous measurement?

# Second star: Considering every single measurement isn't as useful as you expected: there's just too much noise in the
# data. Instead, consider sums of a three-measurement sliding window. Your goal now is to count the number of times the
# sum of measurements in this sliding window increases from the previous sum. Consider sums of a three-measurement
# sliding window. How many sums are larger than the previous sum?

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data
from AoC_tools.work_with_lists import sliding_windows


def is_increasing(data, windows=False, span=None):
    if windows:
        if span is None:
            span = 3
        windows = [sum(window) for window in sliding_windows(data, span)]
    else:
        windows = data
    return [windows[n + 1] - windows[n] > 0 for n in range(len(windows) - 1)]


def count_increases(data, windows=False, span=None):
    return sum(is_increasing(data, windows, span))


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day01.txt', numbers=True)

    if star == 1:  # The final answer is: 1390
        solution = count_increases(data)
    elif star == 2:  # The final answer is: 1457
        solution = count_increases(data, windows=True)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
