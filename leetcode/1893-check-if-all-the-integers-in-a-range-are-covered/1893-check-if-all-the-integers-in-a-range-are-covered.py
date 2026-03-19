"""
- The question: given list of ranges and two integers left and right we are being asked to determine if
- the numbers between the left and right inclusive are betwen at least one of the ranges in side of ranges list.
- Solution:
    - the brute force solution would be creating a continuos list from the ranges in the ranges list
    - and iterating through the left and right + 1 range and check memberships inside the newly created list.
    - this would not be feasible for larger inputs but since our constraints show that the input size is atmost 50 we can do that.
    - to make it slightly ifficient we use set instead of list to store the generated list to check membership.
-  Time and Space complexity:
    - Time => building the set -> O(n*50), since m <= 50, which is O(k), k = right - left + 1 <= 50
            - so the total would be O(n+k) we can remove the k because the k is constant and less than 50,
            - so it will be O(n)
    - space = O(n), due to the creation of the set
"""


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        ranges_set = set()
        for start, end in ranges:
            for i in range(start, end + 1):
                ranges_set.add(i)

        for num in range(left, right + 1):
            if num not in ranges_set:
                return False
        return True
