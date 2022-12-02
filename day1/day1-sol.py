import sys
import os
from typing import *
script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..')
sys.path.append(mymodule_dir)
from helpers import heapUtil, fileUtil

def solution():
    res: List[int] = []
    currSum: int = 0
    data = fileUtil.textTo1DList('data.txt')
    for lines in data:
        converted_lines = str(lines).strip()
        if converted_lines.strip():
            currSum += int(converted_lines)
        else:
            res.append(currSum)
            currSum = 0
    return heapUtil.nthLargestSum(3, res)

print(solution())
