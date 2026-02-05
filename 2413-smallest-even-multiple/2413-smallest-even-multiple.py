"""
- The question: we are asked to find the smalest integer that is a multiple of both 2 and input n.
- Solution:
    - so as we can see there are two possible ways this could go, the first n being even and the second n being odd.
    - if n is even the input n it self is our answer since it is a multiple of it self (n*1) and it is also a multiple of 2 since it is even.
    - else n is odd, the smallest integer that is both multiple of n and 2 is n*2.
    - so we check the parity of the n and we return n or n*2.
-  Time and Space complexity:
    - Time = O(1)
    - space = O(1)
"""


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        return n * 2
