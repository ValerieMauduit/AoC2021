import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day17


def test_best_score():
    assert day17.best_score({'x': [20, 30], 'y': [-10, -5]}) == 45


def test_all_possibilities():
    assert day17.all_initial_velocities({'x': [20, 30], 'y': [-10, -5]}) == 112
