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
    return [
        '{([(<{}[<>[]}>{[]{[(<()>', '[[<[([]))<([[{}[[()]]]', '[{[{({}]{}}([{[{{{}}([]', '[<(<(<(<{}))><([]([]()',
        '<{([([[(<>()){}]>(<<{{',
    ]


@pytest.fixture
def test_found_corrupted():
    values = ['}', ')', ')', ']', '>']
    values.sort()
    return values


def test_find_corrupted(test_data, test_corrupted, test_found_corrupted):
    corruption_check = day10.find_corrupted_lines(test_data)
    corrupted_lines = [corruption['line'] for corruption in corruption_check]
    for corrupted_line in corrupted_lines:
        assert corrupted_line  in test_corrupted
    assert len(corrupted_lines) == len(test_corrupted)

    corrupted_characters = [corruption['character'] for corruption in corruption_check]
    corrupted_characters.sort()
    assert corrupted_characters == test_found_corrupted


def test_score(test_found_corrupted):
    assert day10.score(test_found_corrupted) == 26397
