from typing import Any


class Node:
    def __init__(self, data: Any, next_node):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, data: Any) -> None:
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return

        privious_node = None
        while current_node and current_node.next != data:

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node)
            current_node = current_node.next


if __name__ == '__main__':
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.insert(0)
