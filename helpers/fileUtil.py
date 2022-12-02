from typing import *

def textTo1DList(filepath: str):
    res = []
    with open(filepath, 'r') as f:
        for lines in f:
            stripped = lines.strip()
            res.append(stripped)
    return res