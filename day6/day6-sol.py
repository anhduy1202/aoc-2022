import sys
import os
from typing import *
script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..')
sys.path.append(mymodule_dir)
from helpers import fileUtil

def p1():
    data = fileUtil.textTo1DList("data.txt")
    start = 0
    mySet = set()
    target = 4
    for lines in data:
        for end in range(len(lines)):
            while lines[end] in mySet:
                mySet.remove(lines[start])
                start += 1
            mySet.add(lines[end])
            currLen = (end - start) + 1
            if currLen == target:
                return end + 1      
def p2():
    data = fileUtil.textTo1DList("data.txt")
    start = 0
    mySet = set()
    target = 14
    for lines in data:
        for end in range(len(lines)):
            while lines[end] in mySet:
                mySet.remove(lines[start])
                start += 1
            mySet.add(lines[end])
            currLen = (end - start) + 1
            if currLen == target:
                return end + 1     
print(p1())
print(p2())