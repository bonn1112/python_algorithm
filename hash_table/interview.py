from typing import List, Tuple, Optional


# point -> search pair = use cache

def get_pair(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
    cache = set()
    for num in numbers:
        var = target - num
        if var in cache:  # varがcacheにある場合
            return var, num
        cache.add(num)  # 12 - 11 = 1, 12 - 2 = 10, .... 12 - 10 = 2, which in cache


# def get_pair_half_sum(numbers: List[int]) -> Optional[Tuple[int, int]]:


if __name__ == '__main__':
    l = [11, 2, 5, 9, 10, 3]
    t = 12
    print(get_pair(l, t))
    # print(get_pair_half_sum(l))
