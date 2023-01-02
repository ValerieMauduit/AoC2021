import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day03


@pytest.fixture
def test_data():
    return ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']


def test_gamma_epsilon(test_data):
    assert day03.gamma_epsilon(test_data, 0) == {'gamma': '1', 'epsilon': '0'}
    assert day03.gamma_epsilon(test_data, 1) == {'gamma': '0', 'epsilon': '1'}


def test_binary_power_consumption(test_data):
    assert day03.binary_power_consumption(test_data) == {'gamma': '10110', 'epsilon': '01001'}


def test_score(test_data):
    assert day03.score(test_data) == 198
