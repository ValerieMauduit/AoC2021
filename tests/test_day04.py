import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day04


@pytest.fixture
def test_data():
    return [
        [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1],
        [
            [[22, 13, 17, 11, 0], [8, 2, 23, 4, 24], [21, 9, 14, 16, 7], [6, 10, 3, 18, 5], [1, 12, 20, 15, 19]],
            [[3, 15, 0, 2, 22], [9, 18, 13, 17, 5], [19, 8, 7, 25, 23], [20, 11, 10, 24, 4], [14, 21, 16, 12, 6]],
            [[14, 21, 17, 24, 4], [10, 16, 15, 9, 19], [18, 8, 23, 26, 20], [22, 11, 13, 6, 5], [2, 0, 12, 3, 7]]
        ]
    ]


def test_bingo_card(test_data):
    card = day04.BingoCard(test_data[1][0])
    assert card.values == [
        [22, 13, 17, 11, 0], [8, 2, 23, 4, 24], [21, 9, 14, 16, 7], [6, 10, 3, 18, 5], [1, 12, 20, 15, 19]
    ]
    assert card.win == False
    assert card.drawn == [
        [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False],
        [False, False, False, False, False], [False, False, False, False, False]
    ]
    assert card.width == 5
    assert card.unmarked_sum() == 300


def test_bingo_card_one_turn(test_data):
    card = day04.BingoCard(test_data[1][0])
    card.draw_value(1)
    assert card.drawn == [
        [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False],
        [False, False, False, False, False], [True, False, False, False, False]
    ]
    assert card.win == False
    assert card.unmarked_sum() == 299


def test_bingo_card_wins(test_data):
    card = day04.BingoCard(test_data[1][0])
    card.draw_value(1)
    card.draw_value(22)
    card.draw_value(8)
    card.draw_value(21)
    card.draw_value(6)
    assert card.drawn == [
        [True, False, False, False, False], [True, False, False, False, False], [True, False, False, False, False],
        [True, False, False, False, False], [True, False, False, False, False]
    ]
    assert card.win == True
    assert card.unmarked_sum() == 242


def test_play_bingo(test_data):
    assert day04.play_bingo(test_data[1], test_data[0]) == 4512
