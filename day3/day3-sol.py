import sys
import os
from typing import *
script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..')
sys.path.append(mymodule_dir)
from helpers import fileUtil

# number of rucksacks = total line
# compartment = size of line / 2


def solution():
    lowercase_priority = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
                          "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
                          "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
    priority = {}
    i = 27
    part1_total = 0
    for key in lowercase_priority:
        uppercase_key = key.upper()
        priority[uppercase_key] = i
        i += 1
    priority = lowercase_priority | priority
    data = fileUtil.textTo1DList('data.txt')
    for lines in data:
        first_comp = set(lines[:len(lines) // 2])
        sec_comp = set(lines[(len(lines) // 2):])
        res = ''.join(set(first_comp.intersection(sec_comp)))
        part1_total += priority[res]

    # Part 2
    part2_total = 0
    idx = 1
    group = []
    for lines in data:
        group.append(set(lines))
        if idx % 3 == 0:
            first, sec, third = group
            temp = set(first.intersection(sec))
            res = ''.join(set(temp.intersection(third)))
            part2_total += priority[res]
            group = []
        idx += 1
    return part2_total

print(solution())
