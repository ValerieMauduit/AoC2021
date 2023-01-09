import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day15
from AoC_tools.work_with_maps import AocMap


@pytest.fixture
def test_data():
    return [
        [1, 1, 6, 3, 7, 5, 1, 7, 4, 2], [1, 3, 8, 1, 3, 7, 3, 6, 7, 2], [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
        [3, 6, 9, 4, 9, 3, 1, 5, 6, 9], [7, 4, 6, 3, 4, 1, 7, 1, 1, 1], [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
        [1, 3, 5, 9, 9, 1, 2, 4, 2, 1], [3, 1, 2, 5, 4, 2, 1, 6, 3, 9], [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
        [2, 3, 1, 1, 9, 4, 4, 5, 8, 1]
    ]


def test_best_path(test_data):
    assert day15.best_path_risk(AocMap(test_data)) == 40


def test_best_path_five_times_larger(test_data):
    assert day15.best_path_risk_in_five_times_larger(test_data) == 315

