class RecentCounter:

    def __init__(self):
        self.requests = []
        self.first = 0
        self.count = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.count += 1
        while t - self.requests[self.first] > 3000:
            self.first += 1
            self.count -= 1
    
        return self.count
            
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)