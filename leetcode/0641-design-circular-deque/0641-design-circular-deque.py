class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.length = k
        self.curr_length = 0
        self.head = None
        self.last = None

    def insertFront(self, value: int) -> bool:
        if self.curr_length == self.length:
            return False

        new = Node(value)

        if self.curr_length == 0:
            self.head = self.last = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

        self.curr_length += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.curr_length == self.length:
            return False

        new = Node(value)

        if self.curr_length == 0:
            self.head = self.last = new
        else:
            self.last.next = new
            new.prev = self.last
            self.last = new

        self.curr_length += 1
        return True

    def deleteFront(self) -> bool:
        if self.curr_length == 0:
            return False

        if self.curr_length == 1:
            self.head = self.last = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.curr_length -= 1
        return True

    def deleteLast(self) -> bool:
        if self.curr_length == 0:
            return False

        if self.curr_length == 1:
            self.head = self.last = None
        else:
            self.last = self.last.prev
            self.last.next = None

        self.curr_length -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.curr_length == 0 else self.head.data

    def getRear(self) -> int:
        return -1 if self.curr_length == 0 else self.last.data

    def isEmpty(self) -> bool:
        return self.curr_length == 0

    def isFull(self) -> bool:
        return self.curr_length == self.length


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()