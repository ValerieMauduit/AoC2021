import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day08


@pytest.fixture
def test_data():
    return [
        ['be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb', 'fdgacbe cefdb cefbgd gcbe'],
        ['edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec', 'fcgedb cgb dgebacf gc'],
        ['fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef', 'cg cg fdcagb cbg'],
        ['fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega', 'efabcd cedba gadfec cb'],
        ['aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga', 'gecf egdcabf bgf bfgea'],
        ['fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf', 'gebdcfa ecba ca fadegcb'],
        ['dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf', 'cefg dcbef fcge gbcadfe'],
        ['bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd', 'ed bcgafe cdgba cbgef'],
        ['egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg', 'gbdfcae bgc cg cgb'],
        ['gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc', 'fgae cfgab fg bagce']
    ]


def test_count_unique(test_data):
    assert day08.count_unique(test_data) == 26


def test_get_output_numbers(test_data):
    assert day08.get_output_numbers(test_data) == [8394, 9781, 1197, 9361, 4873, 8418, 4548, 1625, 8717, 4315]
