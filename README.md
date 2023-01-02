# AoC2021

Advent of Code 2021

To run the code:

```commandline
python aoc2021.py --dir dir --day D --star S
```
with:

- dir is the input data directory name
- D is the day number
- S is the star number (1 or 2)

To run all the tests:

```commandline
pytest
```

To run only the tests of a specific day:

```commandline
pytest tests/test_dayXX.py
```

To run only a specific test:

```commandline
pytest tests/test_dayXX.py::my_func
```

## How it went

### Configuration

I do this AoC after December 2021. No stress, no rush. The main idea is to prepare AoC 2023.

First, I need a better testing configuration. I will try to use a regular Pytest setup. I will also keep aside the
useful functions, and try, in general, to really create interesting tools for the future. In particular: to deal with
maps of coordinates + to deal with graphs.

### Day 1: Sonar Sweep

The goal of the day is:

- first make a difference between consecutive numbers in a list.
- then, calculate the sum of a sliding window in a list.

And obviously, as it is the first day, you have to figure out how to read the text files that represent your each day
input.

The problem itself is easy. It's the first day. But it forced me to work with Pytest, which is cool. At the moment, I
only use the basics of it. But still useful. For windowing, I first forgot the last value of my list, and the error
given by pytest was so clear that I fixed it in few seconds.

I think that I will keep the sliding window for the future. Even if it is not a complicated stuff to do again.

### Day 2: Dive!

The first problem needs to parse a little the data, to get a command, composed of a direction (a key-word) plus a value
(a number that I need to transform from string to integer.) In tha AoC, in general, we work with integers.

Not much to say, except that I am so glad to use `pytest`. It is really easy to debug with it. And it forces me to
create interesting functions. I started using parametrization on it, just for fun.