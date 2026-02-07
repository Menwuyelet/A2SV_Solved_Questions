class FrequencyTracker:

    def __init__(self):
        self.data = defaultdict(int)
        self.count = defaultdict(int)

    def add(self, number: int) -> None:
        self.data[number] += 1
        data_freq = self.data[number]
        if data_freq > 1:
            self.count[data_freq] += 1
            self.count[data_freq - 1] -= 1
        else:
            self.count[data_freq] += 1
 
    def deleteOne(self, number: int) -> None:
        if self.data[number] > 0:
            self.data[number] -= 1
            data_freq = self.data[number]
            self.count[data_freq + 1] -= 1
            if data_freq > 0:
                self.count[data_freq] += 1

    def hasFrequency(self, frequency: int) -> bool:
        if self.count[frequency] > 0:
            return True
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)