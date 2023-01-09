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


polymerization = [(
    1, {
        'CH': 1, 'HH': 0, 'CB': 0, 'NH': 0, 'HB': 1, 'HC': 0, 'HN': 0, 'NN': 0, 'BH': 0, 'NC': 1, 'NB': 1, 'BN': 0,
        'BB': 0, 'BC': 1, 'CC': 0, 'CN': 1
    }, 'NCNBCHB'
), (
    4, {
        'CH': 0, 'HH': 1, 'CB': 5, 'NH': 1, 'HB': 0, 'HC': 3, 'HN': 1, 'NN': 0, 'BH': 3, 'NC': 1, 'NB': 9, 'BN': 6,
        'BB': 9, 'BC': 4, 'CC': 2, 'CN': 3
    }, 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'
)]


@pytest.mark.parametrize('steps, polymer, text', polymerization)
def test_insertions(test_data, steps, polymer, text):
    assert day14.insertions(test_data[0], test_data[1], steps) == polymer


scores = [(1, 1), (4, 18), (10, 1588), (40, 2188189693529)]


@pytest.mark.parametrize('steps, result', scores)
def test_score(test_data, steps, result):
    assert day14.score(day14.insertions(test_data[0], test_data[1], steps), test_data[0]) == result
