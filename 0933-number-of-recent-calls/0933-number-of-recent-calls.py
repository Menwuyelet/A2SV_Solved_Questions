"""
- The question: we are tasked to impliment a RecentCounter class that counts the number of requests(calls) made between the range of 3000ms. it have a ping method that accepts a new call and add it to the calls. 
                - ping accepts an argument the time of the call made
- Solution:
    - basicaly what we are tasked is to keep track of the number of calls made to the ping method withn 3000ms
    - we can do that in a couple of ways but the best one is to use qeue.
    - when the requst is made we insert it to our qeue and check if the last call and current the first call in the qeue are in the range of 3000ms.
    - if so we return the len of our qeue for that call.
    - else we pop from our qeue until we meet that condition.

-  Time and Space complexity:
    - Time = O(1), since we use qeue
    - space = O(m), m = the maximum number of calls in the range of 3000ms
"""

class RecentCounter:
    def __init__(self):
        self.request = deque()

    def ping(self, t: int) -> int:
        self.request.append(t)
    
        # we pop from our qeue until we get back to the range.
        while t - self.request[0] > 3000:
            self.request.popleft()

        return len(self.request)
            
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)