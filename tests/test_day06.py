import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day06


@pytest.fixture
def test_data():
    return [3, 4, 3, 1, 2]


fishes = [(1, 0, 5), (2, 1, 6), (3, 1, 7), (4, 2, 9), (18, 4, 26), (80, 571, 5934), (256, 2329711392, 26984457539)]


@pytest.mark.parametrize("days, new_fishes, total", fishes)
def test_create_map(test_data, days, new_fishes, total):
    simulated_fishes = day06.simulate_process(day06.initial_fishes(test_data), days)
    assert simulated_fishes[8] == new_fishes
    assert day06.count_fishes(simulated_fishes) == total
