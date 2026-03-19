"""
- The question: we are given two strings containing a-z english letters and #. # means back space so the element before it and the # are not part of the string. so our task is to determine if the two strings are equal or not.
- Solution:
    - so what we need to do is to remove the backspaces and the element before them from both strings and check if they are equal.
    - to do that we could use two stacks to perform the removal and build stack of only the elements part of the strings and we can check if the two stacks are equal or not. that's it.
-  Time and Space complexity:
    - Time = O(n), n = max(len(s), len(t))
    - space = O(n), 
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        # remove the deleted chrs from string s
        for chr in s:
            if chr != "#":
                stack_s.append(chr)
            
            elif stack_s and chr == "#":
                stack_s.pop()

        # remove the deleted chrs from string t  
        for chr in t:
            if chr != "#":
                stack_t.append(chr)
            
            elif stack_t and chr == "#":
                stack_t.pop()
        
        return stack_s == stack_t