from typing import *

# Determine if one set fullly contain another set
def fullyContainSet(set1, set2):
    return set1.issubset(set2) or set2.issubset(set1)
