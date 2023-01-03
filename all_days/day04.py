# Day 04: Giant Squid

# First star: Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random,
# and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all
# numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)
# The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It
# automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input).
# The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board.
# Then, multiply that sum by the number that was just called when the board won. To guarantee victory against the giant
# squid, figure out which board will win first. What will your final score be if you choose that board?

# Second star: On the other hand, it might be wise to try a different strategy: let the giant squid win. You aren't sure
# how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to
# do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will
# win for sure.
# Figure out which board will win last. Once it wins, what would its final score be?

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import re

from AoC_tools.read_data import read_data


class BingoCard:
    def __init__(self, data):
        self.values = data
        self.drawn = [[False for x in line] for line in data]
        self.win = False
        self.width = len(data)

    def draw_value(self, value):
        for line in range(len(self.values)):
            if value in self.values[line]:
                col = self.values[line].index(value)
                self.drawn[line][col] = True
                self.check_win()

    def check_win(self):
        lines = [sum(line) for line in self.drawn]
        if max(lines) == self.width:
            self.win = True
        else:
            cols = [sum([line[col] for line in self.drawn]) for col in range(self.width)]
            if max(cols) == self.width:
                self.win = True

    def unmarked_sum(self):
        return sum([
            self.values[line][col]
            for line in range(self.width)
            for col in range(self.width)
            if self.drawn[line][col] == False
        ])


def play_bingo(cards, numbers):
    cards = [BingoCard(values) for values in cards]
    numbers = [0] + numbers
    while max([card.win == True for card in cards]) == 0:
        numbers = numbers[1:]
        for card in cards:
            card.draw_value(numbers[0])
    winner = [card.win for card in cards].index(True)
    return cards[winner].unmarked_sum() * numbers[0]


def loose_bingo(cards, numbers):
    cards = [BingoCard(values) for values in cards]
    numbers = [0] + numbers
    while min([card.win == True for card in cards]) == 0:
        looser = [card.win for card in cards].index(False)
        numbers = numbers[1:]
        for card in cards:
            card.draw_value(numbers[0])
    return cards[looser].unmarked_sum() * numbers[0]


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day04.txt', by_block=True, numbers=False)
    draw_numbers = [int(x) for x in data[0][0].split(',')]
    cards = [[[int(x) for x in re.split('[ ]+', line) if x != ''] for line in card] for card in data[1:]]

    if star == 1:  # The final answer is: 41503
        solution = play_bingo(cards, draw_numbers)
    elif star == 2:  # The final answer is: 3178
        solution = loose_bingo(cards, draw_numbers)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
