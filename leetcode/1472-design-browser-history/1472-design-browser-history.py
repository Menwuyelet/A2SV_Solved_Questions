class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.curr = self.head

    def visit(self, url: str) -> None:
        new = Node(url)
        
        # clear forward history
        self.curr.next = None
        
        # link new node
        self.curr.next = new
        new.prev = self.curr
        
        # move the curr to the newly added node
        self.curr = new

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1

        return self.curr.data

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
            
        return self.curr.data

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)