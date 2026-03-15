"""
- The question: we are given two lists of an integer and the four arthimetic oprators in reverse polish notation. we are tasked to evaluate the revers polish notation and return the result.
- Solution:
    - this is classic stack problem.
    - we iterate over the list and everytime we get number as current element we append it to our stack,
    - but when we find oprator as our element we pop two elements from our stack and perform the opration and append the result back to our stack.
    - the one thing is in division we truncate towards zero. so we wont get fractional values.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(n), 
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ["*", "+", "/", "-"]

        for chr in tokens:

            if chr not in op:
                stack.append(int(chr))
            
            else:

                # we pop two of the top elements of the stack and perform the given opration on them and append the result back.
                last = stack.pop()
                first = stack.pop()

                if chr == "+":
                    temp = first + last
                if chr == "-":
                    temp = first - last
                if chr == "*":
                    temp = first * last
                if chr == "/":
                    temp = int(first / last)
                    
                stack.append(temp)
                
        return stack[0]