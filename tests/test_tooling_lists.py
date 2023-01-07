import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools import work_with_lists


@pytest.fixture
def test_data():
    return [12, 42, 73, 1]


def test_sliding_windows(test_data):
    assert work_with_lists.sliding_windows(test_data, 2) == [[12, 42], [42, 73], [73, 1]]
    assert work_with_lists.sliding_windows(test_data) == [[12, 42, 73], [42, 73, 1]]
