import random
from typing import Lis


def select_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        min_index = i
        for j in range(i+1, len_numbers):
            if numbers[min_index] > numbers[j]:
                min_index = j

        numbers[min_index], numbers[i] = numbers[i], numbers[min_index]
    return numbers


if __name__ == '__main__':
    print(select_sort([1, 5, 3, 4, 6]))