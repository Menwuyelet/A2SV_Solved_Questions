"""
- The question: we are tasked to implement qeue using two stacks.
- Solution:
    - really this solution is so easy, it is basically the brute force.
    - we use the two stacks as appending and poping storages.
    - when we append we append to the first stack, and when we pop we reverse that stack to the second stack and the last element(that would be on the top of the second stack) is our first element in qeue.
    - the other thing is when we push we first need to check that there is no elements in the second stack, else we first need to reverse and move them in to the first stack after that we push. 
    - and when we pop we do exact the same thing as pushing but this time from first to the second.
    - and that is it.
-  Time and Space complexity:
    - Time = O(n), n = len(nums in the stack)
    - space = O(n), 
"""

class MyQueue:

    def __init__(self):
        self.enq = []
        self.deq = []

    def push(self, x: int) -> None:

        # we make sure that there are no elements in the deq before we push
        while self.deq:
            self.enq.append(self.deq.pop())
        
        self.enq.append(x)

    def pop(self) -> int:

        # we make sure that there are no elements in enq before we pop
        while self.enq:
            self.deq.append(self.enq.pop())
        
        return self.deq.pop()

    def peek(self) -> int:
        # we do the same thing as pop but we do not remove the element we just copy it
        while self.enq:
            self.deq.append(self.enq.pop())
        
        return self.deq[-1]

    def empty(self) -> bool:

        # we check if either of the stacks have an element if so the qeue is not empty
        return not(self.enq or self.deq)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()