# AoC2021

Advent of Code 2021

To run the code:

```
python aoc2021.py --dir dir --day D --star S
```
with:

- dir is the input data directory name
- D is the day number
- S is the star number (1 or 2)

To run the tests:

```
pytest
```

## How it went

### Configuration

I do this AoC after December 2021. No stress, no rush. The main idea is to prepare AoC 2023.

First, I need a better testing configuration. I will try to use a regular Pytest setup. I will also keep aside the
useful functions, and try, in general, to really create interesting tools for the future. In particular: to deal with
maps of coordinates + to deal with graphs.