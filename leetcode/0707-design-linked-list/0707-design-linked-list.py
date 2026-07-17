class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.len = 0

    def get(self, index: int) -> int:
        if self.len > index:
            cur = self.head
            count = 0
            while count < index:
                count += 1
                cur = cur.next
            return cur.next.val
        return -1

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        new.prev = self.head
        new.next = self.head.next if self.head.next else None
        if new.next:
            new.next.prev = new
        self.head.next = new
        self.len += 1

    def addAtTail(self, val: int) -> None:
        new = Node(val)
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = new
        new.prev = curr
        
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        count = 0
        curr = self.head
        new = Node(val)
        if index <= self.len:
            while count < index:
                curr = curr.next
                count += 1

            new.next = curr.next
            new.prev = curr
            if curr.next:
                curr.next.prev = new
            curr.next = new
            self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < self.len:
            count = 0
            curr = self.head

            while count < index:
                curr = curr.next
                count += 1

            
            curr.next = curr.next.next

            if curr.next:

                curr.next.prev = curr
            self.len -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)