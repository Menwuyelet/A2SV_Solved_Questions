"""
- The question: we are given a list of numbers and tasked to findout if any of the digits are duplicated or not.
- Solution:
    - this is very easy problem, 
    - we just need to see if any of the number appear more than once on the list.
    - to do that we can turn the list in to set and compare the len(num_set) and len(list) and if not equal some number is repeated so we return True else False.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(n), 
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)
        
        return len(nums) > len(num_set)