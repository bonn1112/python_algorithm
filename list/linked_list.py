from typing import Any


class Node:
    def __init__(self, data: Any, next_node=None):
        self.data = data
        self.next = next_node  # listen


class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)  # practice
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:  # how to write, continue the last node is None
            last_node = last_node.next
        last_node.next = new_node
        new_node.next = None

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
        while current_node and current_node.data != data:
            privious_node = current_node
            current_node = current_node.next

        privious_node.next = current_node.next
        current_node = None

        if current_node is None:
            return

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def reverse_iterative(self) -> None:
        current_node = self.head
        privious_node = None

        while current_node:
            new_node = current_node.next
            current_node.next = privious_node

            privious_node = current_node
            current_node = new_node

        self.head = privious_node

    def reverse_recursive(self) -> None:
        def _reverse_recursive(current_node: Node, privious_node: Node):
            if current_node is None:
                return privious_node

            new_node = current_node.next
            current_node.next = privious_node
            privious_node = current_node
            current_node = new_node
            return _reverse_recursive(current_node, privious_node)

        self.head = _reverse_recursive(self.head, None)

    def reverse_even(self) -> None:
        def _reverse_even(head: Node, privious_node: Node):
            if head is None:
                return None

            current_node = head
            while current_node and current_node.data % 2 == 0:
                new_node = current_node.next
                current_node.next = privious_node
                privious_node = current_node
                current_node = new_node

            if current_node != head:
                head.next = current_node
                _reverse_even(current_node, None)
                return privious_node
            else:
                head.next = _reverse_even(head.next, head)
                return head

        self.head = _reverse_even(self.head, None)


if __name__ == '__main__':
    l = LinkedList()
    l.append(2)
    l.append(4)
    l.append(6)
    l.append(1)
    l.append(5)
    l.append(3)
    l.append(6)
    l.append(4)
    l.append(8)
    l.print()
    print('############################')
    l.reverse_even()
    l.print()