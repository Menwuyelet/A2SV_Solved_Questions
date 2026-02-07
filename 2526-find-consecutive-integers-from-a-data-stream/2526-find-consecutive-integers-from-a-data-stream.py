"""
- The question: we are tasked to implement a data stream class that will accept stream of integer and return True if the last k elements are equal specific value.
- Solution:
    - so we can solve this problem by two approachs,
    - in the first approach, we take the inputs put them in deque, add it in to the set we use to verify equality, and increment theire counter.
    - if the deque length is greater that k we pop from the left, decrement the poped data counter and if the counter is 0 we remove it from the set.
    - in every iteration we return the comparation of the set and the value(since the set only contains single digit to be valid).
    - the second approach removes the need for the set, counter and deque entirly and only rely on single variable counter without storing the actual datas.
    - every time we recive new data we check if it is equal to the value, if so we increment the counter by 1.
    - else we reset the counter as the sequence is broken.
    - after each equal to the value condition we check if the counter is greater or equal to the k. if so we return True
    - else we return Fasle for bothnon equal to k and non equal to the value conditions.
-  Time and Space complexity:
    - Time = for both approachs: O(1) for every request so for m request O(m)
    - space = the first approach: O(k)
              the second approach: O(1)
"""

## Approach 1
#  class DataStream:
#     def __init__(self, value: int, k: int):
#         self.value = value
#         self.k = k
#         self.list = deque()
#         self.list_count = defaultdict(int)
#         self.data = set()

#     def consec(self, num: int) -> bool:
#         if len(self.list) >= self.k:
#             val = self.list.popleft()
#             if self.list_count[val] == 1:
#                 self.data.remove(val)
#             self.list_count[val] -= 1

#         self.list.append(num)
#         self.data.add(num)
#         self.list_count[num] += 1
#         if self.k > len(self.list):
#             return False
#         return len(self.data) == 1 and self.value in self.data


## Approach 2
class DataStream:
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
