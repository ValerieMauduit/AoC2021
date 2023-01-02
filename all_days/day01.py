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

def is_increasing(data, windows=False, span=None):
    if windows:
        if span is None:
            windows = sliding_windows(data)
        else:
            windows = sliding_windows(data, span)
    else:
        windows = data
    return [windows[n + 1] - windows[n] > 0  for n in range(len(windows) - 1)]


def count_increases(data, windows=False, span=None):
    return sum(is_increasing(data, windows, span))


def sliding_windows(data, size=3):
    return [sum([data[n + p] for p in range(size)]) for n in range(len(data) - size + 1)]


def run(data_dir, star):
    with open(f'{data_dir}/input-day01.txt', 'r') as fic:
        data = [int(x) for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 1390
        solution = count_increases(data)
    elif star == 2:  # The final answer is: 1457
        solution = count_increases(data, windows=True)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution