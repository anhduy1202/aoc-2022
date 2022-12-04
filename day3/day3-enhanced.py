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
    part1_total = 0
    data = fileUtil.textTo1DList('data.txt')
    for lines in data:
        first_comp = set(lines[:len(lines) // 2])
        sec_comp = set(lines[(len(lines) // 2):])
        res = ''.join(first_comp & sec_comp)
        if (ord(res) < 91):
            part1_total += ord(res) - 38
        else:
            part1_total += ord(res) - 96

    # Part 2
    part2_total = 0
    idx = 1
    group = []
    for lines in data:
        group.append(set(lines))
        if idx % 3 == 0:
            first, sec, third = group
            res = ''.join(first & sec & third)
            if (ord(res) < 91):
                part2_total += ord(res) - 38
            else:
                part2_total += ord(res) - 96
            group = []
        idx += 1
    return part2_total

print(solution())
