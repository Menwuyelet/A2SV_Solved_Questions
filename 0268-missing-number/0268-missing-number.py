"""
- The question: given the list of integers we are tasked to return the number that is in the range of 0 - n, n = len(list)
- Solution:
    - we can solve this problem in tow ways, sorting the list and iterating until we find mismatch or run out of indx and retun the number
    - or convert the list to set and iterate over the range(n+1) and check membership for that number in the set until we find non existing number.
-  Time and Space complexity:
    - Time = using sort: O(n log n + (n+1)) = O(n log n),  using set: O(n + n+1) = O(n)
    - space = using sort: O(n), using set: O(n)
"""

# # Using sort
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         i = 0 
#         while i <= n:
#             if i not in nums:
#                 return i
#             i += 1

# Using set
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set_nums = set(nums)
        for i in range(len(nums)+1):
            if i not in set_nums:
                return i
            

