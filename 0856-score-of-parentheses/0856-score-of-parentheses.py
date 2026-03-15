"""
- The question: we are given a string containing a valid parentheses patern. and we are tasked to calculate the score of the string.
                - "()" has score of 1
                - "()()" has score of 1 + 1
                - "(())" has score of 2 * 1, 1 is the score of the inner parantheses
- Solution:
    - so the hard thing for this problem is that the nested parantheses exist.
    - to calculate and handle these conditions we use stack.
    - and in that stack we score the score of individual parantheses pair.
    - when we find an opning paranthesss we give it a value of 0 and append that value to our stack.
    - when we find a closing parantheses we pop from the stack until we find a value 0(the opning one) and add all the poped values and multiply them by 2 and we replace the value 0(the opning) with that value. 
    - this gives us the score for that parantheses block.
    - but if the top of the stack is already 0 (no nested parantheses) we just replace it with 1 since it is representing one parantheses pair.
    - fo the above example: "(())" our stack would be first iteration : [0], second : [0, 0], third : [0, 1], fourth : [2]
    - after we finish the iteration we return the sum of our stack.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(n), 
"""
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for chr in s:
            if chr == "(":
                stack.append(0)
            else:

                # we check if the current parantheses have a nested childs or not. if so we pop the values of the childs until we find the parent opning and we summ the values of the childs.
                if stack[-1] != 0:
                    temp = 0

                    while stack and  stack[-1] != 0:
                        temp += stack.pop()

                    # we replace the parent opninig with the entire score of that block including the childs.
                    stack[-1] = temp * 2
                
                # if block didnt contain any childrens we simply give it a score of 1
                else:
                    stack[-1] = 1

        return sum(stack)
