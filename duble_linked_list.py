from __future__ import annotations
from typing import Any, Optional


class Node(object):
    def __init__(self, data: Any, next_node: Node = None, prev_node: Node = None) -> None:
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoubleLinkedList(object):
    def __init__(self, head: Node = None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def insert(self, data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def remove(self, data) -> None:
        current_node = self.head
        if current_node and current_node.data == data:
            if current_node.next is None:
                self.head = None
                current_node = None
                return
            else:  # 先頭のデータを消す（次のデータが有る）
                next_node = current_node.next
                next_node.prev = None
                self.head = next_node
                return

        while current_node and current_node.data != data:
            current_node = current_node.next

        if current_node is None:
            return

        if current_node.next is None:#nextnode=none while でcurrent object自体noneになってnextnode cannnot assign
            previous_node = current_node.prev
            previous_node.next = None
            current_node = None
        else:
            next_node = current_node.next
            previous_node = current_node.prev
            previous_node.next = next_node
            next_node.prev = previous_node

    def reverse_iterative(self) -> None:
        current_node = self.head
        if current_node is None:
            return

        previous_node = None
        while current_node:
            new_node = current_node.next  # next入れ忘れ
            current_node.next = previous_node

            previous_node = current_node
            current_node = new_node

        self.head = previous_node

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


if __name__ == '__main__':
    d = DoubleLinkedList()
    d.append(1)
    d.append(2)
    d.append(3)
    d.insert(0)
    d.print()
    print('###########################')
    d.remove(2)
    d.print()
