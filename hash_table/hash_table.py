import hashlib

from typing import Any


class HashTable(object):
    def __init__(self, size=10) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash(self, key) -> int:  # index
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key, value) -> None:
        index = self.hash(key)  # data 格納
        for data in self.table[index]: # indexからlist取り出すlist=[data[0], data[1]]
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[index].append([key, value])

    def print(self) -> None:
        for index in range(self.size): # view all index of table -> List
            print(index, end=' ')
            for data in self.table[index]: # view all list[key, value] data in each index
                print('----->', end=' ')
                print(data, end=' ')

            print() # new line after view one index

    def get(self, key) -> Any:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]

        else:
            return None


if __name__ == '__main__':
    hash_table = HashTable()
    hash_table.add('car', 'Tesla')
    hash_table.add('car', 'Tesla')
    hash_table.add('car', 'Toyota')
    hash_table.add('pc', 'Mac')
    hash_table.add('sns', 'YouTube')
    hash_table.print()
    # print(hash_table.get('sns'))
