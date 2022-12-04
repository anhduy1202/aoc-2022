import sys
import os
from typing import *
script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..')
sys.path.append(mymodule_dir)
from helpers import fileUtil

def solution():
    data = fileUtil.textTo1DList('data.txt')
    part1_res = 0
    part2_res = 0
    dup_range = lambda temp1, temp2: range(temp1, temp2 + 1)

    for lines in data:
        stripped = lines.split(",")
        left, right = stripped
        left1 = left.split("-")
        right1 = right.split("-")
        temp1 = set(dup_range(int(left1[0]),int(left1[-1])))
        temp2 = set(dup_range(int(right1[0]), int(right1[-1])))
        subset = temp1 - temp2
        subset2 = temp2 - temp1
        subset3 = temp1 & temp2
        if len(subset) == 0 or len(subset2) == 0:
            part1_res += 1
        if len(subset3) > 0:
            part2_res += 1
    return (part1_res, part2_res)

print(solution())