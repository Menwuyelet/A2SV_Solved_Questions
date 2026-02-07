"""
- The question: we are tasked to implement a FrequencyTracker class that have three methods add, deletone and hasFrequency.
               - this class will count the frequency of teh data that it stores and perform the three tasks.
- Solution:
    - to design this datastructure we use two dictionaries, one to sotre the actual data and their freq and the second to store the amount of elements that are with specific frequency.
    - so the first dictionary stores the data as key and its frequency as value.
    - the second will store the frequency as key and number of elements with that specific frequency.
    - when we add new element we add it to the data dictionary and increment its freq by 1,
    - after that we subtract 1 from the frequency that specific data had and add 1 to the new frequency the dat now have 
      (if the prev frequency was 0 meaning the data is new we just add to the new freq which is 1)
    - when we delete an element we reduce 1 from the current frequency and we add 1 to the new frequency
      (if the current freq is 1 we just simple reduce 1 from it and do not add to any thing since it is completly of the data and its freq is 0)
    - when we check if specific freq have a data that appears at that freq we check the second dict and return true if the value is 1 or greater else false.
-  Time and Space complexity:
    - Time = O(1) per opration, O(n), n = number of oprations
    - space = O(k + m) = > O(m), k = number of distinct data, m = frequency range
"""

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