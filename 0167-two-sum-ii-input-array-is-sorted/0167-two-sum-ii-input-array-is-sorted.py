"""
- The question: we are given a list of integers and a target, and we are tasked to find the two numbers that sum up to that target from the given list. and the list is sorted in increasing order.
- Solution:
    - the brute force solution would be to iterate over all the numbers and find their sum with every other number on the list.
    - to do that we can use nested loops and iterate over the list n^2 times.
    - but since our list is sorted we can use collieding pointers.
    - we start one ptr at 0 and the other at n-1, then we check the sum of the two index values and if it is less than target we increment our first ptr by one, else we decrement our ptr by one.
    - we break the code when the two ptrs reach eachother or we find two indexes with the sum equal to our target.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(1), 
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                break
        return([l+1, r+1])
