"""
- The question: given a string of parenthesis we are tasked to determin if the given string is valid parentheris or not.
- Solution:
    - to say a given parenthesis is valid or not we should check that every opning chr have a closing one and vice versa.
    - to do that in implimentation we can use stack.
    - we iterate throught the s and if the current chr is opning we append it to our stack 
    - else it is closing we check our stack ensuring it is not empty and we also check the top element is the valid opning chr for our current closing chr.
    - if one of teh two upper conditions fail we return false
    - after finishing the iteration with out break, we chek if the stack is empty or not 
    - if so we return true else we return false
-  Time and Space complexity:
    - Time = O(n), n = len(s)
    - space = O(n), 
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = {")": "(", "}":"{", "]":"["}

        # we iterate over the s and check the three coditions to perform an action 
        for chr in s:
            if chr in ["(", "[", "{"]:
                stack.append(chr)
            else:

                # if there is no element left on stack or the element at the top is not the correct opning parenthersis we return false and stop
                if not stack or stack[-1] != key[chr]:
                    return False
                else:
                    stack.pop()
        
        # if there is an element left in teh stack it means there is an opening chr with out a closing one
        if stack:
            return False

        return True