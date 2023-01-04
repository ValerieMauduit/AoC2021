import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day09


@pytest.fixture
def test_data():
    return ['2199943210', '3987894921', '9856789892', '8767896789', '9899965678']


def test_low_points(test_data):
    low_points = day09.get_low_points(test_data)
    low_points.sort()
    assert len(low_points) == 4
    assert low_points == [0, 1, 5, 5]


def test_risk_level():
    assert day09.risk_level([0, 1, 5, 5]) == 15
