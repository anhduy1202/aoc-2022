import sys
import os
from typing import *
script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..')
sys.path.append(mymodule_dir)
from helpers import fileUtil, algoUtil


def solution():
    data = fileUtil.textTo1DList('data.txt')
    part1_res = 0
    part2_res = 0

    for lines in data:
        left, right = lines.split(",")
        left1, right1 = left.split("-"), right.split("-")
        temp1 = set(range(int(left1[0]), int(left1[-1]) + 1))
        temp2 = set(range(int(right1[0]), int(right1[-1]) + 1))
        subset = temp1 & temp2
        if algoUtil.fullyContainSet(temp1, temp2):
            part1_res += 1
        if len(subset) > 0:
            part2_res += 1
    return (part1_res, part2_res)


print(solution())
