"""
- The question: given two lists we are tasked if the lists are equal or not. lists are equal if they contain the same elements
              - with the same ammount. meaning duplicates also must be the same.
- Solution:
    - to check firs if the two lists contain the same elements we can use set.
    - we convert them to set and check if they are equal (meaning contain the same element)
    - but this is not enogh as we also need to check not only elements but also the number of they appear.
    - to do that we can use counter and check if the two counters are equal.
    - so if both return true then the two lists are equl else not.
-  Time and Space complexity:
    - Time => O(n+m), n = len(a), m = len(m)
    - space = O(n+m)
"""

from collections import Counter


class Solution:
    def checkEqual(self, a, b) -> bool:
        # code here
        set_a = set(a)
        set_b = set(b)
        if set_a != set_b:
            return False

        count_a = Counter(a)
        count_b = Counter(b)
        return count_a == count_b
