"""
- The question: given list of numbers and an integer k, we are tasked to find the number of pair of indices(i,j) such that nums[i] == nums[j] and(i*j)%k == 0
- Solution:
    - since our constraint allows it we use the bruteforce approach.
    - we use nested loop with hold and seek ptrs and iterate through the list and check the condition.
    - if the condition is meet we add 1 to our counter.
-  Time and Space complexity:
    - Time = O(n^2), n = len(nums),
    - space = O(1)
"""
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0

        for hold in range(len(nums) - 1):
            for seek in range(hold+1, len(nums)):
                if nums[hold] == nums[seek] and (hold*seek)%k == 0:
                    count +=1

        return count
