class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = {")": "(", "}":"{", "]":"["}
        for chr in s:
            if chr in ["(", "[", "{"]:
                stack.append(chr)
            else:
                if not stack or stack[-1] != key[chr]:
                    return False
                else:
                    stack.pop()
        
        if stack:
            return False

        return True