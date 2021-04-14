import math
import os
import random
import re
import sys

from typing import List


def partition(numbers: List[int], low: int, high: int) -> int:
    pivot = numbers[low]
    i = low
    for j in range(low+1, high):
        if pivot >= numbers[j]:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i], numbers[low] = numbers[low], numbers[i]

    return i + 1


def quicksort(length: int, numbers: List[int]) -> None:
    def _quicksort(numbers: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = partition(numbers, low, high)
            _quicksort(numbers, low, partition_index -1)
            print(numbers[low:partition_index -1])
            _quicksort(numbers, partition_index + 1, high)
            print(numbers[partition_index + 1: high])

    _quicksort(numbers, 0, length)


if __name__ == '__main__':
    arr = [5, 8, 1, 3, 7, 9, 2]

    quicksort(7, arr)
