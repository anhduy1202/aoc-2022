from typing import *
import os
import sys
script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..')
sys.path.append(mymodule_dir)
from helpers import fileUtil

def solution():
    opponent: OrderedDict[str, int] = OrderedDict({"A": 1, "B": 2, "C": 3})
    player: OrderedDict[str, int] = OrderedDict({"X": 1, "Y": 2, "Z": 3})
    totalScore: int = 0
    data = fileUtil.textTo1DList('data.txt')
    for lines in data:
        row: List[str] = lines.split(' ')
        left, right = row
        # PART 2 
        if right == "Y":  # need to draw
            totalScore += opponent[left] + 3
        elif right == "X":  # need to lose
            if left == "B": totalScore += 1
            elif left == "A": totalScore += 3
            else: totalScore += 2
        elif right == "Z": # need to win
            if left == "A": totalScore += 2 + 6
            elif left == "B": totalScore += 3 + 6
            else: totalScore += 1 + 6
        # PART 1
        elif opponent[left] == player[right]:  # Draw
            totalScore += (player[right] + 3)
        elif (left == "A" and right == "Y") or (left == "B" and right == "Z") or (left == "C" and right == "X"): # win
            totalScore += (player[right] + 6)
        else: # lose
            totalScore += player[right]
    return totalScore

print(solution())
