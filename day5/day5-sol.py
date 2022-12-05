from typing import *
from collections import deque
import re

def removeSquareBracket():
    with open("input_data.txt", 'r') as f:
        data = f.read()
    #remove square brackets
    data = data.replace("[", "").replace("]", "")
    with open("parsed_data.txt", 'w') as f:
        f.write(data)

# PART 1
def solution_p1():
    storages = {i: deque() for i in range(1,10)}
    position = {k:v for k,v in zip(range(0,36,4),range(1,10))}
    p1_res = ''
    with open("parsed_data.txt", 'r') as f:
        data = f.read()
        # Parse input
        crates, instructions = data.split("\n\n")
        crates_split = crates.splitlines()[:-1]
        # Create queue by column
        for crate in crates_split:
            for i in range(len(crate)):
                if crate[i] != " ":
                    storages[position[i]].append(crate[i])
        # follow instruction
        instructions_split = instructions.splitlines()
        for instruction in instructions_split:
            result = re.findall(r"\d+", instruction)
            amount, start, end = result
            for i in range(int(amount)):
                if len(storages[int(start)]) == 0: # Empty stack
                    break
                # Move one stack to another 
                popout = storages[int(start)].popleft()
                storages[int(end)].appendleft(popout)
        for key in storages:
            p1_res += storages[key][0] if storages[key] else ''
        return p1_res

# PART 2
def solution_p2():
    storages = {i: deque() for i in range(1,10)}
    position = {k:v for k,v in zip(range(0,36,4),range(1,10))}
    p2_res = ''
    with open("parsed_data.txt", 'r') as f:
        data = f.read()
        # Parse input
        crates, instructions = data.split("\n\n")
        crates_split = crates.splitlines()[:-1]
        # Create queue by column
        for crate in crates_split:
            for i in range(len(crate)):
                if crate[i] != " ":
                    storages[position[i]].append(crate[i])
        # follow instruction
        instructions_split = instructions.splitlines()
        for instruction in instructions_split:
            result = re.findall(r"\d+", instruction)
            amount, start, end = result
            counter = int(amount)
            print(counter)
            temp = deque()
            for i in range(int(amount)):
                if len(storages[int(start)]) == 0: # Empty stack
                    break
                temp.appendleft(storages[int(start)].popleft())
                counter += 1
            storages[int(end)].extendleft(temp)
        for key in storages:
            p2_res += storages[key][0] if storages[key] else ''
        return p2_res

print(solution_p1())