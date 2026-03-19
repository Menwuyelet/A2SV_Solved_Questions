"""
- The question: given a list integers we are tasked to return the integer that only appears 1 time in the list when the other appear exactly two times.
- Solution:
    - this is very easy counting problem, we can solve it by sorting the list and iterating through the list and check every consiquetive digits until we find the single one.
    - but this approach takes O(n log n) time and there is aconstraint that states to solve it using O(n) time and O(1) space
    - to come up with solution we can use XOR opration.
    - this is because when we XOR the same digits they canle out leaving the single number alone.
    - this solution gives us O(n) time and O(1) space complesity.
-  Time and Space complexity:
    - Time =  Sorting: O(n log n), XOR: O(n)
    - space = Sorting: O(1), XOR: O(1)
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return use_XOR(nums)


def use_sort(nums):
    nums.sort()
    i = 0
    while i < len(nums) - 1:
        if nums[i] != nums[i+1]:
            return nums[i]
        i += 2
    return nums[-1]


def use_XOR(nums):
    ans = 0
    for num in nums:
        ans = ans ^ num
    return ans