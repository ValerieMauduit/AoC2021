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


rates = [({'gamma': '10110', 'epsilon': '01001'}, 198), ({'oxygen': '10111', 'co2': '01010'}, 230)]


@pytest.mark.parametrize("binary_values, score", rates)
def test_score(binary_values, score):
    assert day03.get_score(binary_values) == score


def test_oxygen_rate(test_data):
    assert day03.binary_oxygen_rate(test_data) == '10111'


def test_co2_rate(test_data):
    assert day03.binary_co2_rate(test_data) == '01010'
