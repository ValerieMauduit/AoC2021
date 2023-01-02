# Day 02: Dive!

# First star: Now, you need to figure out how to pilot this thing. It seems like the submarine can take a series of
# commands like forward 1, down 2, or up 3. Note that since you're on a submarine, down and up affect your depth, and so
# they have the opposite result of what you might expect. The submarine seems to already have a planned course (your
# puzzle input). You should probably figure out where it's going.
# Calculate the horizontal position and depth you would have after following the planned course. What do you get if you
# multiply your final horizontal position by your final depth?

# Second star: description

def get_position(data):
    position_dict = {'forward': 0, 'up': 0, 'down': 0}
    for command in [x.split(' ') for x in data]:
        position_dict[command[0]] += int(command[1])
    return [position_dict['forward'], position_dict['down'] - position_dict['up']]


def score(position):
    return position[0] * position[1]


def debugged_position(data):
    position_dict = {'aim': 0, 'depth': 0, 'horizontal': 0}
    for command in [x.split(' ') for x in data]:
        if command[0] == 'down':
            position_dict['aim'] += int(command[1])
        elif command[0] == 'up':
            position_dict['aim'] -= int(command[1])
        elif command[0] == 'forward':
            position_dict['horizontal'] += int(command[1])
            position_dict['depth'] += int(command[1]) * position_dict['aim']
        else:
            raise Exception(f"The command {command[0]} is not recognized.")
    return [position_dict['horizontal'], position_dict['depth']]


def run(data_dir, star):
    with open(f'{data_dir}/input-day02.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 1762050
        solution = score(get_position(data))
    elif star == 2:  # The final answer is: 1855892637
        solution = score(debugged_position(data))
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
