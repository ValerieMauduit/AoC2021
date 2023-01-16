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

The two problems need to parse a little the data, to get a command, composed of a direction (a key-word) plus a value
(a number that I need to transform from string to integer.) In tha AoC, in general, we work with integers. And then,
quite simple operations to do.

Not much to say, except that I am so glad to use `pytest`. It is really easy to debug with it. And it forces me to
create interesting functions. I started using parametrization on it, just for fun.

### Day 3: Binary Diagnostic

You have a list of binary numbers, and you need to do a test along the columns of bits. The thing I had to get was the
binary transformation which is easy in python:

```python
int(my_string, base)
```

For the second part, I had to separate the function that really defines the most common bit in a column. Once done, I
only needed to be careful to end my while loop (as usual).

### Day 4: Giant Squid

The goal is to play bingo here. It was fun to build a `BingoCard` class and its methods, and easy to use. But I
struggled with my too many levels of sub-lists in lists. Once done, it was OK for the first part.

With the way I built my stuff, it was straightforward to play until everybody wins. I only had to take care of keeping
the index of the loosing bingo card. I like to name my classes, variables and functions as in the AoC story. It is
funnier to read and debug. And also more understandable.

I always use the same kind of pretty print to debug. Why don't I add it in my tools? I need to figure out a way to
provide something really useful for it.

```python
for line in data:
    print(line)
    # or
    print(''.join(line))
print(' ')
```

### Day 5: Hydrothermal Venture

It is really time-consuming to do a good tooling for my AoC. But I think that my next AoC will deserve this time. Plus:
it is nice, and I learn with it. This day is the first day of this AoC with a map. I had so many things to improve in my
map class: 
- deal with an origin which is not at [0, 0],
- build an empty map, or a map to put some points based on coordinates,
- get or set a specific point in a map (obviously, with an origin that may not be [0, 0])

Once done, translating this problem in my map wasn't difficult. The most difficult was to parse the data in a way that
allowed me to read the clouds lines.

For the second part, I guessed that I would have to deal with the diagonals. I thought it would be straightforward, but
it wasn't. My algorithm would have created square clouds with these diagonals coordinates. So I had to have a second
case for these clouds. And as usual, I first tested with an algorithm that "forgot" the last point of each diagonal
cloud.

### Day 6: Lanternfish

Here, we need to count some elements with a rule to change the data of the list at each step. The text shows it with a
change for each element. But actually, I immediately realized that the elements were of 9 values, and it would be better
to group them in a dict, saying how many of each type I have. It worked well (for the first star). My only problem was
that I didn't realize immediately that there were two different way to get fishes of type 6, so I need to add the two
results.

I didn't use any of my specific tools, but I used a parametric test, and it was useful to understand my mistake.

Actually, as I used a map, the second star was totally straightforward. I **love** when my first implementation works
directly for the second star.

### Day 7: The Treachery of Whales

Lol, it is exactly a regression problem, with minimization of the absolute error. I did it without any DS library,
because we don't need. It was easy except the fact that I first tested on my data of the day 6...

For the second star, I immediatly remembered that the formula is `n * (n + 1) / 2`. But I didn't realize first that, as
I needed to get an absolute value, I really needed to calculate `abs(n) + 1`, not `abs(n + 1)`. My second error then was
that to get a minimum, I initialized with a number that I knew it was higher than the solution. OK for the first star...
but for the second one, my initialization number was too low, before I fixed it.

What I liked: assign a function to a variable, to use the same mechanism for the two stars, with a different fuel
consumption formula.

### Day 8: Seven Segment Search

_I realize that if I want to be fast, I should create all my days files + the main program with all the days before
starting December._

It is about some patterns that must allow finding out which letter corresponds to which object. The first star is easy,
but we might think that the second one will be to really get the patterns and use them to decode some numbers.

For the second star, it was funny to figure out what are the conditions for a code to be such or such digit. You have to
think "What is the direction to take?" Finally, I had to first count the number of letters of the code (star 1) then
figure out if a letter appear a certain amount of time on the left side. I think that it would have been possible (but
more difficult) even if on the side, we wouldn't have got all the ten digits each time.

### Day 9: Smoke Basin

Here, we have a kind of heatmap, with numerical values on all the coordinates. How to find values that are lower than
their neighbours?

I improved a bit my `AocMap` class, to be able to deal with numbers in it. It was so cool to use it! I definitively
need it for next year.

For the second part, I had to improve the `AocMap` once again. Cross fingers that it will be helpful in the future. Once
done, I can fully concentrate on solving the problem, which is really fun. My idea now is : **never navigate** in a map,
always update it (or a parallel map) with the possible values and summarize it in the end. Here, I put a number to each
low point and a wall to each 9. Then from neighbour to neighbour, I expand the basins numbers. Finally, I count the
instances of each basin value to determine which are the largest ones.

### Day 10: Syntax Scoring

First recursion of the season, with a problem of checking if parenthesis close or not. It is really a typical exercise
for a coding interview. Working on AoC improves a lot my skills in recursion. The second part is only a variation, not a
more difficult exercise, I think.

### Day 11: Dumbo Octopus

Here, we work again with a map. It is a map of numbers and the process to change the numbers is a chained reaction. So
be careful to do it correctly.

Once again I need some improvements to my `AocMap` class. Then, my most important question was: were to put the flash
count? Because in the beginning I wanted to increase it whenever a neighbour of the octopus is impacted by the flash,
which was false.

For the second part, I copied-pasted the same code with only a small change in the stop condition. Not very clean :(

### Day 12: Passage Pathing

The idea here is to count the number of paths in a graph, with a simple rule first, and then a more complicated one.

OK, first graph. Fight your fears. I created a small AocGraph class. I am not sure yet that it will be useful for the
future. I also created a function to navigate in a graph. It isn't configurable, but I think that it can help me to be
able to copy-paste and then modify it. Let's see.

Second star: I **really** need to go back on it and fix! It is so ugly. I don't understand why at the moment, but I
authorize going twice in any small cave. And then, I post-process the result to count only the travels when I go twice
in at most one small cave.

Finally, I fixed it, by using the now famous deeper first. So nice and more understandable (at least for me).

### Day 13: Transparent Origami

It is a funny map: you have the coordinates of black dots of a map, and you fold it many times. At the end, you can read
a message on the folded map.

OK, as usual: first create interesting methods for mt `AocMap`: extract a submap, reverse a map, superpose two maps.
Once did, the code is so simple! It is *not* a solution during the month of December, because it is longer at the
moment, my idea is really to build tools that I can use for next December.

The other good idea, as usual, is not to forget to use the `sets` to reduce a list to its unique elements, or to know if
there are some duplicate elements in a list.

During the second star, I realized that:
- When I fold, I keep the line of the line of the fold in my maps. Not good.
- When I remove it when I get the submaps, the origins of my submaps don't belong anymore.
- When I force the origins of my submaps after each fold, I have an error on the real data, but not on the test.

Finally, I removed the last column or the last line after getting the submaps. Not perfect in my opinion, but not the
worse to do.

### Day 14: Extended Polymerization

Once again a typical AoC problem: you have a list (or a string) and a process that increases it a lot. You do some steps
and then post-process the result to get a score.

I added some list facilities, and I think that they are pretty cool. But I have an error in the number of steps, and I
don't really get it: I need 10 steps in the test of the day, but 11 to get the right answer in the real problem. Let's
let as it for the moment.

The second star is not surprising: more steps. But even on the test example, it doesn't run immediately. So I need to
find another way to do it, and I guess that as always, I would need to use a dict.

I fixed it for a dict. To get the dict of the polymer step n was OK. But to calculate the score was more complicated. I
first calculated the occurrences of the pairs, which is not what we want. The occurrences of each element in the
pairs. But it is almost the double of the values I need. *Almost* is the problem: I count twice each element, except the
first and the last one. When I realized it, I added the first and the last element of the polymer template, before
dividing the score by two! Yes, because the first and the last element never change during the polymerization. OK, I
obtained a result. And guess what? My first star value was too high... because now, I need to use the real number of
steps. I fixed a bug, but I don't know how. It is like the story of the engineers comings from a good, a medium and a
bad university (adaptable for each country, in France we tell it with Polytechnique, Centrale and the one the teller is
from):
- The engineer from Centrale designs a bridge. The bridge collapses and she doesn't know why.
- The engineer from Polytechnique designs a bridge.  The bridge collapses and she does know why.
- The engineer from the other school (me!) designs a bridge. The bridge doesn't collapse, but she doesn't know why.

### Day 15: Chiton

The goal is to find the path that minimizes a score, in a map of numbers. I got it very fast but I was surprised: why is
only once check in all the initial map enough?

But concerning the second star... I cannot be proud of it. I guessed first 2939, which was too high. The 2935, with a
while loop to try to reduce my score. It was too low. But the two values are so close that... I got the final answer
with a dichotomy process.

### Day 17: Trick Shot

The goal here is to find out the best way to launch a projectile, in order to:
- reach a given zone
- maximize the altitude reached before going down

I thought that it would be easy. But in fact no. First, I needed a new move in my `AocMap` and I thought "Great! I will
have a new cool method for the displacements in my map." I struggled. Because I had an error in taking into account an
origin of my map which is not [0, 0]. Because I tested only on origin changes where `x_origin == y_origin`. And I had
mixed the x and the y in a formula.

Then I modelled a trajectory and it was OK. Then I tried to find the best one. My main problems:
- When the place above the origin wasn't height enough, it blocked and the result was false,
- When I increased my map in all directions, it was too large, I had to figure out which are *really* the directions I
  wanted to increase (above the start of the trajectory, and in a small measure, on the right of the map.)
- What is the stop condition to consider that the initial vertical speed is too high? I decided to check if I either
  finish in the target, either finish with my max reachable x and a y which in below the target. First thing: to have a
  stop condition, I had to inverse my continue condition, and I made a lot of errors when doing it. And then... I
  discovered that it was possible to go in one of these conditions at a moment, but a slightly higher initial vertical
  speed could reach the target zone again...

My new idea is that the problem, actually, is solvable by arithmetic operations. Let's call the initial speed [vx, vy],
and the step n.
- x: the positions are vx * (vx + 1) / 2 - (vx - n + 1) * (vx - n) / 2 until n > vx, then it is vx * (vx + 1) / 2
- maximal height: it is vy * (vy + 1) / 2
- y: we start to decrease (from the maximal height) when n > vy and then, the global decrease from this point is
  (n - vy) * (n - vy + 1) / 2 at each step.

With these values, I should be able to:
- determine the values of vx when we horizontally reach the target zone
- determine the values of vy when we vertically reach the target zone

In the end, I determined all the vy to reach the target zone vertically and then tested if there was a vx value
available to reach the zone at the same step. Some formulas on paper, no map. OK...

Then I thought that the second part, count all the initial velocities to reach the goal, would be easy. But some points
were important:
- I counted the number of steps to reach the target. I had to avoid counting twice when I reach the target and the next
  step is again in the target.
- Be careful of some thresholds in the loops, as always.

Honestly, sometimes coding in Pycharm, with Pytest, is not the most comfortable. Then I code in Jupyter and I output
many things. Here, I even copied my results in OpenOffice Calc and checked one by one my results with the forecasted one
to understand that I had some doubles, then a forgotten number of steps...

### Day 18: Snailfish

Here we have some specific rules to a snailfish addition. It was long to understand the rules. I also checked manually
on an example, to be sure I understood them correctly. I see these nested lists as a list of numbers with altitudes. I
will try to work this way. Let's see.

And it worked, after some iterations on small bugs, like "is it the index, or the index + 1?"
