import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day02


@pytest.fixture
def test_data():
    return ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']


def test_get_position(test_data):
    assert day02.get_position(test_data) == [15, 10]


def test_debugged_position(test_data):
    assert day02.debugged_position(test_data) == [15, 60]


test_position = [([15, 10], 150), ([15, 60], 900)]


@pytest.mark.parametrize("position, score", test_position)
def test_score(position, score):
    assert day02.score(position) == score
