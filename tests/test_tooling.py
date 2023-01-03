import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools import work_with_lists, work_with_maps


@pytest.fixture
def test_data():
    return [12, 42, 73, 1]


def test_sliding_windows(test_data):
    assert work_with_lists.sliding_windows(test_data, 2) == [[12, 42], [42, 73], [73, 1]]
    assert work_with_lists.sliding_windows(test_data) == [[12, 42, 73], [42, 73, 1]]


@pytest.fixture
def test_map():
    return work_with_maps.AocMap(['....#.', '...##.', '#.....'], [5, 1])


def test_map_creation(test_map):
    assert test_map.map == [
        ['.', '.', '.', '.', '#', '.'], ['.', '.', '.', '#', '#', '.'], ['#', '.', '.', '.', '.', '.']
    ]
    assert test_map.width == 6
    assert test_map.height == 3
    assert test_map.x == 5
    assert test_map.y == 1


def test_map_position(test_map):
    assert test_map.position() == [5, 1]


def test_map_moves(test_map):
    test_map.move('U')
    assert (test_map.x, test_map.y) == (5, 0)
    test_map.move('U')
    assert (test_map.x, test_map.y) == (5, 0)
    test_map.move('D')
    assert (test_map.x, test_map.y) == (5, 1)
    test_map.move('D')
    assert (test_map.x, test_map.y) == (5, 2)
    test_map.move('R')
    assert (test_map.x, test_map.y) == (5, 2)
    test_map.move('L')
    assert (test_map.x, test_map.y) == (4, 2)
    test_map.move('L')
    assert (test_map.x, test_map.y) == (3, 2)


def test_map_changes(test_map):
    test_map.change_point(1, 1, '*')
    assert test_map.map == [
        ['.', '.', '.', '.', '#', '.'], ['.', '*', '.', '#', '#', '.'], ['#', '.', '.', '.', '.', '.']
    ]
    test_map.change_points([[2, 2], [5, 2], [4, 0]], 'o')
    assert test_map.map == [
        ['.', '.', '.', '.', 'o', '.'], ['.', '*', '.', '#', '#', '.'], ['#', '.', 'o', '.', '.', 'o']
    ]


def test_map_neighbours(test_map):
    neighbours = test_map.neighbours()
    assert len(neighbours) == 5
    assert sum([n == '.' for n in neighbours]) == 3
    assert sum([n == '#' for n in neighbours]) == 2
    assert test_map.count_neighbours('.') == 3
    assert test_map.count_neighbours('#') == 2
    test_map.x, test_map.y = 1, 1
    neighbours = test_map.neighbours()
    assert len(neighbours) == 8
    assert sum([n == '.' for n in neighbours]) == 7
    assert sum([n == '#' for n in neighbours]) == 1
    assert test_map.count_neighbours('.') == 7
    assert test_map.count_neighbours('#') == 1

