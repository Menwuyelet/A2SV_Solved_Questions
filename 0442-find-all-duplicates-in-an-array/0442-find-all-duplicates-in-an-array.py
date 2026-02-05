"""
- The question: given a list of numbers we are tasked to find numbers that appear twice on the list.
               - the solution should run on O(n) time and O(1) space additional to the space used to store the output.
- Solution:
    - we can solve this problem by iterating through the list one time and store their count.
-  Time and Space complexity:
    - Time =  O(n)
    - space = O(n)
"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return use_sign(nums)



# using dictionary O(n) time and O(n) space
# def use_dict(nums):
#     count = {"two": []}
#     for num in nums:
#         count[num] = count.get(num, 0) + 1
#         if count[num] > 1:
#             count["two"].append(num)
#             count.pop(num)
#     return count["two"]

def use_sign(nums):
    ans = []
    for x in nums:
        index = abs(x) - 1
        if nums[index] < 0:
            ans.append(abs(x))
        nums[index] = -nums[index]
    return ans