import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day11


@pytest.fixture
def test_data():
    return [
        '5483143223', '2745854711', '5264556173', '6141336146', '6357385478', '4167524645', '2176841721', '6882881134',
        '4846848554', '5283751526'
    ]


def test_10steps(test_data):
    step10 = [
        [0, 4, 8, 1, 1, 1, 2, 9, 7, 6], [0, 0, 3, 1, 1, 1, 2, 0, 0, 9], [0, 0, 4, 1, 1, 1, 2, 5, 0, 4],
        [0, 0, 8, 1, 1, 1, 1, 4, 0, 6], [0, 0, 9, 9, 1, 1, 1, 3, 0, 6], [0, 0, 9, 3, 5, 1, 1, 2, 3, 3],
        [0, 4, 4, 2, 3, 6, 1, 1, 3, 0], [5, 5, 3, 2, 2, 5, 2, 3, 5, 0], [0, 5, 3, 2, 2, 5, 0, 6, 0, 0],
        [0, 0, 3, 2, 2, 4, 0, 0,0, 0]
    ]
    run_10steps = day11.run_steps(test_data, 10)
    assert run_10steps['map'] == step10
    assert run_10steps['flashes'] == 204


def test_100steps(test_data):
    assert day11.run_steps(test_data, 100)['flashes'] == 1656
