import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day00


@pytest.fixture
def test_data():
    return [12, 42, 73]


def test_my_func(test_data):
    assert day00.my_func(test_data) == 127
