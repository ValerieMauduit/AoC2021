import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day12
from AoC_tools.work_with_graphs import AocGraph


caves = [
    ([['start', 'A'], ['start', 'b'], ['A', 'c'], ['A', 'b'], ['b', 'd'], ['A', 'end'], ['b', 'end']], 10),
    (
        [
            ['dc', 'end'], ['HN', 'start'], ['start', 'kj'], ['dc', 'start'], ['dc', 'HN'], ['LN', 'dc'], ['HN', 'end'],
            ['kj', 'sa'], ['kj', 'HN'], ['kj', 'dc']
        ],
        19
    ),
    (
        [
            ['fs', 'end'], ['he', 'DX'], ['fs', 'he'], ['start', 'DX'], ['pj', 'DX'], ['end', 'zg'], ['zg', 'sl'],
            ['zg', 'pj'], ['pj', 'he'], ['RW', 'he'], ['fs', 'DX'], ['pj', 'RW'], ['zg', 'RW'], ['start', 'pj'],
            ['he', 'WI'], ['zg', 'he'], ['pj', 'fs'], ['start', 'RW']
        ],
        226
    )
]


@pytest.mark.parametrize("paths, count", caves)
def test_count_paths(paths, count):
    assert day12.count_paths(AocGraph(paths)) == count


def test_count_paths_visit_twice():
    test_data = [['start', 'A'], ['start', 'b'], ['A', 'c'], ['A', 'b'], ['b', 'd'], ['A', 'end'], ['b', 'end']]
    assert day12.count_paths_visit_twice(AocGraph(test_data)) == 36
