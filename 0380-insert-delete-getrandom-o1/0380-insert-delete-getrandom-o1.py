class RandomizedSet:

    def __init__(self):
        self.data = {}
        self.list = []
        self.last = 0
    def insert(self, val: int) -> bool:
        if val not in self.data:
            self.data[val] = self.last
            self.list.append(val)
            self.last += 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False

        idx = self.data[val]
        last_element = self.list[self.last - 1]

        # move last element to idx
        self.list[idx] = last_element
        self.data[last_element] = idx

        # remove last
        self.list.pop()
        self.data.pop(val)
        self.last -= 1

        return True


    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()