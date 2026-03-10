class DataStream:

    def __init__(self, value: int, k: int):
        self.counter = defaultdict(int)
        self.list = deque()
        self.k_count = 0
        self.k = k
        self.val = value

    def consec(self, num: int) -> bool:
        self.counter[num] += 1
        self.list.append(num)
        self.k_count += 1

        if self.k_count > self.k:
            val = self.list.popleft()
            self.k_count -= 1
            self.counter[val] -= 1

            if self.counter[val] == 0:
                del(self.counter[val])
        
        return len(self.counter.keys()) == 1 and self.k_count == self.k and self.list[0] == self.val
    


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)