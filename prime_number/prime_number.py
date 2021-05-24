# n = 1 => return 2
# n = 4 => return 7
# n = 10 => return 29

from typing import List, Generator

import time


def generate_prime_number_v1(n: int) -> List[int]:
    primes = []
    for i in range(2, n + 1):  # 2-50
        for j in range(2, i):  # i = 10 -> 10 % 2 == 0 break
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


def generate_prime_number_v2(n: int) -> List[int]:
    primes = []
    cache = {}
    for i in range(2, n + 1):
        is_prime = cache.get(i)
        if is_prime is False:
            continue  # for にもどる
        primes.append(i)
        cache[i] = True
        for j in range(i * 2, n + 1, i):
            cache[j] = False
    return primes


def generate_prime_number_v3(n: int) -> Generator[int, None, None]:
    cache = {}
    for i in range(2, n + 1):
        is_prime = cache.get(i)
        if is_prime is False:
            continue  # for にもどる
        yield i
        cache[i] = True
        for j in range(i * 2, n + 1, i):
            cache[j] = False

if __name__ == '__main__':
    start = time.time()
    print(generate_prime_number_v1(50))
    print(time.time()-start)

    start = time.time()
    print(generate_prime_number_v2(50))
    print(time.time() - start)

    start = time.time()
    print([i for i in generate_prime_number_v3(50)])
    print(time.time() - start)