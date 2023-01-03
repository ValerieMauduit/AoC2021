import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day05


@pytest.fixture
def test_data():
    return [
        '0,9 -> 5,9', '8,0 -> 0,8', '9,4 -> 3,4', '2,2 -> 2,1', '7,0 -> 7,4', '6,4 -> 2,0', '0,9 -> 2,9', '3,4 -> 1,4',
        '0,0 -> 8,8', '5,5 -> 8,2'
    ]


maps = [
    (
        False,
        [
            ['.', '.', '.', '.', '.', '.', '.', 1, '.', '.'], ['.', '.', 1, '.', '.', '.', '.', 1, '.', '.'],
            ['.', '.', 1, '.', '.', '.', '.', 1, '.', '.'], ['.', '.', '.', '.', '.', '.', '.', 1, '.', '.'],
            ['.', 1, 1, 2, 1, 1, 1, 2, 1, 1], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], [2, 2, 2, 1, 1, 1, '.', '.', '.', '.']
        ],
        5
    ), (
        True,
        [
            [1, '.', 1, '.', '.', '.', '.', 1, 1, '.', ], ['.', 1, 1, 1, '.', '.', '.', 2, '.', '.', ],
            ['.', '.', 2, '.', 1, '.', 1, 1, 1, '.', ], ['.', '.', '.', 1, '.', 2, '.', 2, '.', '.', ],
            ['.', 1, 1, 2, 3, 1, 3, 2, 1, 1, ], ['.', '.', '.', 1, '.', 2, '.', '.', '.', '.', ],
            ['.', '.', 1, '.', '.', '.', 1, '.', '.', '.', ], ['.', 1, '.', '.', '.', '.', '.', 1, '.', '.', ],
            [1, '.', '.', '.', '.', '.', '.', '.', 1, '.', ], [2, 2, 2, 1, 1, 1, '.', '.', '.', '.', ]
        ],
        12
    )
]


@pytest.mark.parametrize("diagonals, result_map, score", maps)
def test_create_map(test_data, diagonals, result_map, score):
    assert day05.create_map(test_data, diagonals).map == result_map


@pytest.mark.parametrize("diagonals, result_map, score", maps)
def test_score(diagonals, result_map, score):
    assert day05.count_overlaps(result_map) == score