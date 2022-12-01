import heapq
from typing import *


def nthLargestSum(n: int, data: List[int]):
    return sum(heapq.nlargest(n, data))
