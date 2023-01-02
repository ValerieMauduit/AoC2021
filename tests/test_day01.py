import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day01


@pytest.fixture
def test_data():
    return [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_is_decreasing(test_data):
    assert day01.is_increasing(test_data) == [True, True, True, False, True, True, True, False, True]


def test_count_increases(test_data):
    assert day01.count_increases(test_data) == 7


def test_sliding_windows(test_data):
    assert day01.sliding_windows(test_data) == [607, 618, 618, 617, 647, 716, 769, 792]


def test_count_increases_with_windows(test_data):
    assert day01.count_increases(test_data, True) == 5
