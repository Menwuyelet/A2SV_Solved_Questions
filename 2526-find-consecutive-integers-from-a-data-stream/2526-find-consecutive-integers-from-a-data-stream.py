class DataStream:
    from collections import deque
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.list = deque()
        self.list_count = defaultdict(int)
        self.data = set()

    def consec(self, num: int) -> bool:
        if len(self.list) == self.k:
            val = self.list.popleft()
            if self.list_count[val] == 1:
                self.data.remove(val)
            self.list_count[val] -= 1

        self.list.append(num)
        self.data.add(num)
        self.list_count[num] += 1
        if self.k > len(self.list):
            return False
        return len(self.data) == 1



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)