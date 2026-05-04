"""
- The question: we are given a pile of candies and number of students to allocate the candies equaly to all the students and return that equal number.
- Solution:
    - so what we are going to do is try every number of candies starting from 1 to the max of the candies pile and check if there is a number that is the max that gives equal number of candies to all students.
    - so what we do is we divied all the candy piles for that number and add all the result and check if they are greater or equal to the number of students.
    - so to optimize the approach we can use binary search on the number we gona devide the piles by to find the optimal number fast and bringing the time complexity form O(n^2) to O(n log m)
-  Time and Space complexity:
    - Time = O(n log m), n = number of candy pile, m = maximum pile of the candy 
    - space = O(1), 
"""

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        start = 1
        end = max(candies)
        res = 0

        # we iterate over smallest posible value and maximum posible value in binary search mode to check if it is the number
        while start <= end:

            # we find the currnt number we are going to try
            mid = (end+start)//2

            # we calculate the amount of studetns gona get candy if we use this number as our max candy
            count = sum(pile//mid for pile in candies)

            # if it is greater or equal than our number of students we try greater number 
            if count >= k:
                res = mid
                start = mid + 1

            # else we try smaller number 
            elif count < k:
                end = mid - 1

        return res
