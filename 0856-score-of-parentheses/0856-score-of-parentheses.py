class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for chr in s:
            if chr == "(":
                stack.append(0)
            else:
                if stack[-1] != 0:
                    temp = 0
                    while stack and  stack[-1] != 0:
                        temp += stack.pop()
                
                    stack[-1] = temp * 2
                else:
                    stack[-1] = 1
        return sum(stack)
