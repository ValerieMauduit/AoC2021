import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day13


@pytest.fixture
def test_data():
    return [
        [
            [6, 10], [0, 14], [9, 10], [0, 3], [10, 4], [4, 11], [6, 0], [6, 12], [4, 1], [0, 13], [10, 12], [3, 4],
            [3, 0], [8, 4], [1, 10], [2, 14], [8, 10], [9, 0]
        ],
        ['fold along y=7', 'fold along x=5']
    ]


def test_count_visible_dots_one_fold(test_data):
    assert day13.count_visible_dots(test_data[0], [test_data[1][0]]) == 17
