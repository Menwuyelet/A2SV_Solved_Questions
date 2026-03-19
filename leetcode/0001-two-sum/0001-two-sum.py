"""
- The question: we are given a list of integers and a target, and we are tasked to find the two numbers that sum up to that target from the given list.
- Solution:
    - the brute force solution would be to iterate over all the numbers and find their sum with every other number on the list.
    - to do that we can use nested loops and iterate over the list n^2 times.
    - but we have another way, using a dictionary we can store all the numbers in dictionary as key and theire indexe as value.
    - after that we iterate over the numbers and calculate the diffrence of target - curren number and if that number is present in the dictinary 
    - that means we found our two numbers and return their indexes.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(n), 
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDic = {}
        for i in range(len(nums)):
            numsDic[nums[i]] = i
        
        for i in range(len(nums)):
            number = target - nums[i]
            if number in numsDic and numsDic[number] != i:
                return(i, numsDic[number])