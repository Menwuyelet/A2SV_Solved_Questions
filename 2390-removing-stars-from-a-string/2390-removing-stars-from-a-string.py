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