"""
- The question: we are given two lists and tasked to return the union of the two lists
- Solution:
    - to solve this problem we can iterate through one of the lists and check the membership in the other list and if it exists we append it to our union list
    - but in this problem the lists may contain duplicates and if an element is duplicated we only count it once.
    - and this approch is not optimal.
    - the other way to do it is by using set. we convet both lists to sets and use union oprator to get elements that are found in both lists.
    - this also covers the duplicate constratint as sets store non duplicate values.
-  Time and Space complexity:
    - Time = O(n+m), n = len of list a, m = len of list b
    - space = O(n+m),
"""


class Solution:
    def findUnion(self, a, b):
        # code here
        set_a = set(a)
        set_b = set(b)
        return set_a | set_b
