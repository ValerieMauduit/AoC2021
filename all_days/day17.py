# Day 17: Trick Shot

# First star: The probe launcher on your submarine can fire the probe with any integer velocity in the x (forward) and y
# (upward) directions. The probe's x,y position starts at 0,0. Then, it will follow some trajectory by moving in steps.
# On each step, these changes occur in the following order:
# - The probe's x position increases by its x velocity.
# - The probe's y position increases by its y velocity.
# - Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater
#   than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
# - Due to gravity, the probe's y velocity decreases by 1.
# For the probe to successfully make it into the trench, the probe must be on some trajectory that causes it to be
# within a target area after any step. The submarine computer has already calculated this target area (your puzzle
# input). Find the initial velocity that causes the probe to reach the highest y position and still eventually be within
# the target area after any step. What is the highest y position it reaches on this trajectory?

# Second star: description

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


def best_score(data):
    y_min, y_max = - data['y'][1], - data['y'][0]
    x_min, x_max = data['x'][0], data['x'][1]
    # I first calculate all the initial vertical speeds that allow to go in the zone
    y_possible = []
    for vy in range(y_max * 2):
        max_height = vy * (vy + 1) / 2
        n = 0
        y_last = - max_height
        while (y_last <= y_max) & (n * (n + 1) / 2 < 2 * (y_max + max_height)):
            n += 1
            y_last = - max_height + n * (n + 1) / 2
            if (y_last >= y_min) & (y_last <= y_max):
                # I keep the max_height and the count of the steps to go inside the zone (vertically)
                y_possible += [[max_height, vy + n]]
    # Now I find the last value in y_possible that can be reached horizontally
    # I loop on the initial vx to get the zone in the given number of steps
    vx = 0
    while vx < x_max:
        x_position_last_step = vx * (vx + 1) / 2 - max([vx - y_possible[-1][1], 0]) * (vx - y_possible[-1][1] + 1) / 2
        if x_position_last_step < x_min:
            # If vx is too small I increase it
            vx += 1
        elif x_position_last_step <= x_max:
            print(y_possible[-1])
            return y_possible[-1][0]
        else:
            # If I missed the zone, I take the previous y solution and start again from 0
            y_possible = y_possible[:-1]
            vx = 0


def all_initial_velocities(data):
    y_min, y_max = - data['y'][1], - data['y'][0]
    x_min, x_max = data['x'][0], data['x'][1]
    # I first calculate all the initial vertical speeds that allow to go in the zone
    y_possible = {}
    # For positive vy means going down
    for vy in range(y_max + 1):
        n = 0
        y_last = 0
        while y_last <= y_max:
            n += 1
            y_last = (vy + n - 1) * (vy + n) / 2 - vy * (vy - 1) / 2
            if (y_last >= y_min) & (y_last <= y_max):
                # I keep vy and the count of the steps to go inside the zone (vertically)
                if n in y_possible:
                    y_possible[n] += [vy]
                else:
                    y_possible[n] = [vy]
    # For positive vy mean going up
    for vy in range(1, y_max * 2):
        max_height = vy * (vy + 1) / 2
        n = 0
        y_last = - max_height
        while (y_last <= y_max) & (n * (n + 1) / 2 < 2 * (y_max + max_height)):
            n += 1
            y_last = - max_height + n * (n + 1) / 2
            if (y_last >= y_min) & (y_last <= y_max):
                # I keep vy and the count of the steps to go inside the zone (vertically)
                if vy + n + 1 in y_possible:
                    y_possible[vy + n + 1] += [- vy]
                else:
                    y_possible[vy + n + 1] = [- vy]
    # Now I loop on vx to find out the values where I can reach the zone and their counts of steps
    x_possible = {}
    for vx in range(x_max + 1):
        for n in range(max(y_possible) + 1):
            x = vx * (vx + 1) / 2 - max([vx - n, 0]) * (vx - n + 1) / 2
            if (x >= x_min) & (x <= x_max):
                if n in x_possible:
                    x_possible[n] += [vx]
                else:
                    x_possible[n] = [vx]
    possibilities = []
    for n in range(max([3 * y_max, x_max]) + 1):
        if (n in x_possible) & (n in y_possible):
            for x in x_possible[n]:
                for y in y_possible[n]:
                    if (x, y) not in possibilities:
                        possibilities += [(x, y)]
    return len(possibilities)


def run(star):
    data = {'x': [169, 206], 'y': [-108, -68]}

    if star == 1:  # The final answer is: 5778
        solution = best_score(data)
    elif star == 2:  # The final answer is: 2576
        solution = all_initial_velocities(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
