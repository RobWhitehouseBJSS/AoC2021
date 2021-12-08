from collections import Counter
from functools import reduce
from pathlib import Path

INPUT_PATH = Path("input.txt")

segment_lengths = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


def with_length(clues, l):
    return {s for s in clues if len(s) == l}


def comp(clue):
    return frozenset("abcdefg") - clue


def solve_clues(clues):
    one = with_length(clues, 2).pop()
    print(one)
    four = with_length(clues, 4).pop()
    seven = with_length(clues, 3).pop()
    eight = with_length(clues, 7).pop()

    zero_six_nine = with_length(clues, 6)
    six = [s for s in zero_six_nine if comp(s) < one][0]
    zero_nine = zero_six_nine - {six}
    zero = [s for s in zero_nine if comp(s) < four][0]
    nine = (zero_nine - {zero}).pop()

    two_three_five = with_length(clues, 5)
    three = [s for s in two_three_five if one < s][0]
    two_five = two_three_five - {three}
    five = [s for s in two_five if s < nine][0]
    two = (two_five - {five}).pop()
    print([zero, one, two, three, four, five, six, seven, eight, nine])
    return [zero, one, two, three, four, five, six, seven, eight, nine]


counter = Counter()
with open(INPUT_PATH, "r") as f:
    for line in f:
        _, digits = line.split(" | ")
        counter.update(map(len, digits.strip().split()))
print(sum(counter[segment_lengths[d]] for d in [1, 4, 7, 8]))

outs = []
with open(INPUT_PATH, "r") as f:
    for line in f:
        clue_strings, digits = line.split(" | ")
        clues = [frozenset(string) for string in clue_strings.split()]
        solutions = solve_clues(clues)
        digits = [solutions.index(frozenset(string)) for string in digits.strip().split()]
        outs.append(reduce(lambda l, r: 10 * l + r, digits))
print(sum(outs))