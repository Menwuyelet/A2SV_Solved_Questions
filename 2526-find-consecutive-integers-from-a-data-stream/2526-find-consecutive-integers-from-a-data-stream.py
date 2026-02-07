class DataStream:
    from collections import deque
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.counter = 0

    def consec(self, num: int) -> bool:
        if self.value == num:
            self.counter += 1
            if self.counter >= self.k:
                return True
        else:
            self.counter = 0
        return False



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)