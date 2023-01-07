import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools import work_with_lists, work_with_maps, read_data


@pytest.fixture
def test_data():
    return [12, 42, 73, 1]

@pytest.fixture
def test_map():
    return work_with_maps.AocMap(['....#.', '...##.', '#.....'], [5, 1])

@pytest.fixture
def test_line():
    return "20-22, 21-87"

@pytest.fixture
def test_coordinates():
    return [[1, 5], [3, 2]]


def test_sliding_windows(test_data):
    assert work_with_lists.sliding_windows(test_data, 2) == [[12, 42], [42, 73], [73, 1]]
    assert work_with_lists.sliding_windows(test_data) == [[12, 42, 73], [42, 73, 1]]


def test_map_creation(test_map):
    assert test_map.map == [
        ['.', '.', '.', '.', '#', '.'], ['.', '.', '.', '#', '#', '.'], ['#', '.', '.', '.', '.', '.']
    ]
    assert test_map.width == 6
    assert test_map.height == 3
    assert test_map.x == 5
    assert test_map.y == 1


def test_empty_map_build():
    my_map = work_with_maps.AocMap.empty_from_size(3, 4)
    assert my_map.map == [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    assert my_map.width == 3
    assert my_map.height == 4


def test_map_from_coord(test_coordinates):
    without_origin = work_with_maps.AocMap.from_coord(test_coordinates)
    assert without_origin.origin == [1, 2]
    assert without_origin.map == [['.', '.', '#'], ['.', '.', '.'], ['.', '.', '.'], ['#', '.', '.']]
    with_origin = work_with_maps.AocMap.from_coord(test_coordinates, x_min=0, x_max=5, y_min=0, y_max=5)
    assert with_origin.origin == [0, 0]
    assert with_origin.map == [
        ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '#', '.', '.'],
        ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '#', '.', '.', '.', '.']
    ]


def test_map_position(test_map):
    assert test_map.get_position() == [5, 1]


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
    test_map.set_point([1, 1], '*')
    assert test_map.map == [
        ['.', '.', '.', '.', '#', '.'], ['.', '*', '.', '#', '#', '.'], ['#', '.', '.', '.', '.', '.']
    ]
    test_map.set_points([[2, 2], [5, 2], [4, 0]], 'o')
    assert test_map.map == [
        ['.', '.', '.', '.', 'o', '.'], ['.', '*', '.', '#', '#', '.'], ['#', '.', 'o', '.', '.', 'o']
    ]


def test_map_neighbours(test_map):
    neighbours = test_map.get_neighbours()
    assert len(neighbours) == 5
    assert sum([n == '.' for n in neighbours]) == 3
    assert sum([n == '#' for n in neighbours]) == 2
    assert test_map.count_neighbours('.') == 3
    assert test_map.count_neighbours('#') == 2
    test_map.x, test_map.y = 1, 1
    neighbours = test_map.get_neighbours()
    assert len(neighbours) == 8
    assert sum([n == '.' for n in neighbours]) == 7
    assert sum([n == '#' for n in neighbours]) == 1
    assert test_map.count_neighbours('.') == 7
    assert test_map.count_neighbours('#') == 1


def test_map_origin(test_map):
    test_map.origin = [-1, -2]
    test_map.set_position([0, 0])
    test_map.set_point([1, 0], 'o')
    assert test_map.map == [
        ['.', '.', '.', '.', '#', '.'], ['.', '.', '.', '#', '#', '.'], ['#', '.', 'o', '.', '.', '.']
    ]
    assert test_map.count_neighbours('.') == 3
    assert test_map.count_neighbours('#') == 1
    assert test_map.count_neighbours('o') == 1


def test_read_data_without_split():
    assert read_data.read_data('tests/input_test.txt', numbers=True, by_block=True) == [[12, 156], [1], [42, 42, 3]]
    assert read_data.read_data('tests/input_test.txt', numbers=True, by_block=False) == [12, 156, 1, 42, 42, 3]
    assert (read_data.read_data('tests/input_test.txt', numbers=False, by_block=False) ==
            ['12', '156', '', '1', '', '42', '42', '3'])
    assert (read_data.read_data('tests/input_test.txt', numbers=False, by_block=True) ==
            [['12', '156'], ['1'], ['42', '42', '3']])


def test_read_data_with_split():
    assert (read_data.read_data('tests/input_test_for_splits.txt', numbers=True, split=' ') ==
            [[12, 13, 14], [1, 2, 3], ['45-42'], [67]])
    assert (read_data.read_data('tests/input_test_for_splits.txt', numbers=False, split=' ') ==
            [['12', '13', '14'], ['1', '2', '3'], ['45-42'], ['67']])
    assert (read_data.read_data('tests/input_test_for_splits.txt', numbers=True, split='-') ==
            [['12 13 14'], ['1 2 3'], [45, 42], [67]])
    assert (read_data.read_data('tests/input_test_for_splits.txt', numbers=False, split='-') ==
            [['12 13 14'], ['1 2 3'], ['45', '42'], ['67']])
    with pytest.raises(Exception) as exc_info:
        read_data.read_data('tests/input_test_for_splits.txt', by_block=True, split='-')
    assert len(exc_info.value.args[0]) > 0


def test_smart_split(test_line):
    assert read_data.smart_split(test_line, "-|, ") == ["20", "22", "21", "87"]
    assert read_data.smart_split([test_line, test_line], "-|, ") == [["20", "22", "21", "87"], ["20", "22", "21", "87"]]
