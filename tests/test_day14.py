import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day14


@pytest.fixture
def test_data():
    return [
        'NNCB',
        {
            'CH': 'B', 'HH': 'N', 'CB': 'H', 'NH': 'C', 'HB': 'C', 'HC': 'B', 'HN': 'C', 'NN': 'C',
            'BH': 'H', 'NC': 'B', 'NB': 'B', 'BN': 'B', 'BB': 'N', 'BC': 'B', 'CC': 'N', 'CN': 'C'
        }
    ]


polymerization = [(1, 'NCNBCHB'), (4, 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB')]


@pytest.mark.parametrize('steps, polymer', polymerization)
def test_insertions(test_data, steps, polymer):
    assert day14.insertions(test_data[0], test_data[1], steps) == polymer


scores = [(1, 1), (4, 18), (10, 1588)]


@pytest.mark.parametrize('steps, result', scores)
def test_score(test_data, steps, result):
    assert day14.score(day14.insertions(test_data[0], test_data[1], steps)) == result
