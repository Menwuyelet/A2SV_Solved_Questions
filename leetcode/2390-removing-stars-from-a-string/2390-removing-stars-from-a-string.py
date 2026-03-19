"""
- The question: we are given a sting consisting of lower english letters and star. and we are tasked to remove the left most near character when we find a star.
- Solution:
    - to solve this we can use stack efficiently.
    - we can iterate through the string and when we find a non star chr we append it to the stack.
    - but when we find a star we pop from our stack.
    - after finishing this we join the stack and return it.
-  Time and Space complexity:
    - Time = O(n), n = len(s)
    - space = O(n), 
"""
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for chr in s:

            # if we reach a star in our string we remove the closeset none star chr to its left.
            if chr == "*":
                stack.pop()
            else:
                stack.append(chr)
        
        return "".join(stack)