import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day07


@pytest.fixture
def test_data():
    return [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


moves = [(2, 37), (1, 41), (3, 39), (10, 71)]


@pytest.mark.parametrize("position, fuel", moves)
def test_fuel_spent(test_data, position, fuel):
    assert day07.fuel_spent(test_data, position) == fuel


fixed_moves = [(2, 206), (5, 168)]


@pytest.mark.parametrize("position, fuel", fixed_moves)
def test_fuel_spent_fixed(test_data, position, fuel):
    assert day07.fuel_spent_fixed(test_data, position) == fuel
