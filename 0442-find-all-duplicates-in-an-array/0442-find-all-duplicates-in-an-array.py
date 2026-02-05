"""
- The question: given a list of numbers we are tasked to find numbers that appear twice on the list.
               - the solution should run on O(n) time and O(1) space additional to the space used to store the output.
- Solution:
    - we can solve this problem by iterating through the list one time and store the 
-  Time and Space complexity:
    - Time = using sort: O(n log n + (n+1)) = O(n log n),  using set: O(n + n+1) = O(n)
    - space = using sort: O(n), using set: O(n)
"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = {"two": []}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > 1:
                count["two"].append(num)
                count.pop(num)
        return count["two"]