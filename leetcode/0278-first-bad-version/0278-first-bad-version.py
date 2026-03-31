# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

"""
- The question: we are given a number n and an api isBadVersion which returns a boolean if the number we give it is bad it returns True else False. we are tasked to find the first bad element.
- Solution:
    - the brute force is to iterate until we get our very first bad version and that is it.
    - but we have a large input so it will TLE
    - so we can reduce the number of calls by using binary search
    - we start with the n as our top and 1 as our low and call our api every time we get a new mid.
    - but since we are tasked to find the very first we should check if the number before our mid is not bad so the mid to be answer.
    - if it is not the first we do the binary search again until we find our first bad or finish our range.

- Time and Space complexity:
    - Time = O(log n), n = len(nums)
    - space = O(1), 
"""

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = (right + left) // 2

            # we make sure that the mid is bad but the mid - 1 is not to make sure it is first bad.
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid

            elif isBadVersion(mid):
                right = mid - 1

            else:
                left = mid + 1