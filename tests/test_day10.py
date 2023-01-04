import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day10


@pytest.fixture
def test_data():
    return [
        '[({(<(())[]>[[{[]{<()<>>', '[(()[<>])]({[<{<<[]>>(', '{([(<{}[<>[]}>{[]{[(<()>', '(((({<>}<{<{<>}{[]{[]{}',
        '[[<[([]))<([[{}[[()]]]', '[{[{({}]{}}([{[{{{}}([]', '{<[[]]>}<{[{[{[]{()[[[]', '[<(<(<(<{}))><([]([]()',
        '<{([([[(<>()){}]>(<<{{', '<{([{{}}[<[[[<>{}]]]>[]]'
    ]


@pytest.fixture
def test_corrupted():
    corrupted = [
        '{([(<{}[<>[]}>{[]{[(<()>', '[[<[([]))<([[{}[[()]]]', '[{[{({}]{}}([{[{{{}}([]', '[<(<(<(<{}))><([]([]()',
        '<{([([[(<>()){}]>(<<{{',
    ]
    corrupted.sort()
    return corrupted


@pytest.fixture
def test_found_corrupted():
    values = ['}', ')', ')', ']', '>']
    values.sort()
    return values


@pytest.fixture
def test_found_incomplete():
    return [
        '[({(<(())[]>[[{[]{<()<>>', '[(()[<>])]({[<{<<[]>>(', '(((({<>}<{<{<>}{[]{[]{}', '{<[[]]>}<{[{[{[]{()[[[]',
        '<{([{{}}[<[[[<>{}]]]>[]]'
    ]


@pytest.fixture
def test_additions():
    return ['}}]])})]', ')}>]})', '}}>}>))))', ']]}}]}]}>', '])}>']


def test_find_corrupted(test_data, test_corrupted, test_found_corrupted):
    corruption_check = day10.find_corrupted_lines(test_data)
    corrupted_lines = [corruption['line'] for corruption in corruption_check]
    corrupted_lines.sort()
    assert corrupted_lines == test_corrupted

    corrupted_characters = [corruption['character'] for corruption in corruption_check]
    corrupted_characters.sort()
    assert corrupted_characters == test_found_corrupted


def test_corruption_score(test_found_corrupted):
    assert day10.corruption_score(test_found_corrupted) == 26397


def test_find_incomplete(test_data, test_found_incomplete):
    incomplete = day10.find_incomplete_lines(test_data)
    incomplete.sort()
    expected = test_found_incomplete
    expected.sort()
    assert incomplete == expected


def test_complete_sequence(test_found_incomplete, test_additions):
    for n in range(len(test_found_incomplete)):
        assert day10.complete_line(test_found_incomplete[n]) == test_additions[n]


def test_completion_score(test_additions):
    assert day10.completion_score(test_additions) == 288957

