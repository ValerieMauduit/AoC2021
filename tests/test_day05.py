import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day05


@pytest.fixture
def test_data():
    return [
        '0,9 -> 5,9', '8,0 -> 0,8', '9,4 -> 3,4', '2,2 -> 2,1', '7,0 -> 7,4', '6,4 -> 2,0', '0,9 -> 2,9', '3,4 -> 1,4',
        '0,0 -> 8,8', '5,5 -> 8,2'
    ]

@pytest.fixture
def test_map():
    return [
        ['.', '.', '.', '.', '.', '.', '.', 1, '.', '.'], ['.', '.', 1, '.', '.', '.', '.', 1, '.', '.'],
        ['.', '.', 1, '.', '.', '.', '.', 1, '.', '.'], ['.', '.', '.', '.', '.', '.', '.', 1, '.', '.'],
        ['.', 1, 1, 2, 1, 1, 1, 2, 1, 1], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], [2, 2, 2, 1, 1, 1, '.', '.', '.', '.']
    ]


def test_create_map(test_data, test_map):
    assert day05.create_map(test_data).map == test_map


def test_score(test_map):
    assert day05.count_overlaps(test_map) == 5