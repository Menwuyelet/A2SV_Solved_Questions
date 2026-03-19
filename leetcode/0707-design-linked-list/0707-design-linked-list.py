class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.dummy = Node(0)
        self.length = 0


    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        curr = self.dummy.next

        for _ in range(index):
            curr = curr.next

        return curr.val


    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.dummy.next
        self.dummy.next = node
        self.length += 1


    def addAtTail(self, val: int) -> None:
        curr = self.dummy

        while curr.next:
            curr = curr.next

        curr.next = Node(val)
        self.length += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return

        curr = self.dummy

        for _ in range(index):
            curr = curr.next

        node = Node(val)
        node.next = curr.next
        curr.next = node

        self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return

        curr = self.dummy

        for _ in range(index):
            curr = curr.next

        curr.next = curr.next.next

        self.length -= 1