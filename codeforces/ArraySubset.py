"""
- The question: we are given two lists and tasked to findout if list b is subset of list a.
- the numbers of times the element appear in both lists matter.
- Solution:
    - because duplication matters we can't use set and set oprations.
    - istead we use counter to count the elements of both lists and compare them and see if the counter of
    - element in list b is greater than counter of element in list a.
    - if so we return false meaning not subset.
-  Time and Space complexity:
    - Time = O(n+m), n = len(a), m = len(b)
    - space = O(n+m)
"""

from collections import Counter


class Solution:
    def isSubset(self, a, b):
        count_a = Counter(a)
        count_b = Counter(b)

        for x in count_b:
            if count_b[x] > count_a.get(x, 0):
                return False
        return True
