"""
- The question: we are tasked to design a datastructure tahat perform insertion, deletion and getrandom in O(1).
- and the get random method should be really random.
- Solution:
    - to solve this problem we could use set and impliment all the method in O(1), but the getRandom method would not be truly random.
    - to fix that we could use list and dictionary together.
    - we store the values and their index on the list on the dictinary, and when we remove a value we first swap it with the last element and delete the last element.
    - this way it will become O(1).
    - when we add new element we append it at last and store its index in the dictinary.
    - to impliment get random we can use random.choice(list) this will produce a truly random element.
-  Time and Space complexity:
    - Time = O(1), for each opration.
    - space = O(n), n = len(values added)
"""

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

        self.list[idx] = last_element
        self.data[last_element] = idx

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
