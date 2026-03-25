"""
- The question: we are given a codeded string with the code format of english letter in angle braces and the number of times they appear in the original string as a cofficient and tasked to return the original string the decoded one.

- Solution:
    - what we are being tasked is to decode the string. so we can iterate over the string and decode it chr by char.
    - the problem with this approach is what if there are nested chrs inside of a braces. so we use stack to decode every thing that is enclosed by a braces.
    - what we do is we iterate through the string and when we hit a number we initiate the decoding state and we append the chr that is inside of the braces multiply it with the coefficient and put it on our ans.
-  Time and Space complexity:
    - Time = O(n), n = len(s) since the max num is no more than 300
    - space = O(n), 
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            
            # we append every chr we find from the coded string unless it is closing brace 
            if s[i] != "]":
                stack.append(s[i])
            else:
                
                # we pop from our stack until we find the opning brace and construct our sub segment we are decoding
                sub = ""
                while stack[-1] != "[":
                    sub = stack.pop() + sub

                # we remove the opning brace
                stack.pop()

                # we construct the multiplying number and convert it in to int
                num = ""
                while stack and stack[-1] in ["0","1","2","3","4","5","6","7","8","9"]:
                    num = stack.pop() + num
                
                inum = int(num)

                # we decode our segment and add it to our temp ans.
                temp = sub * inum

                # we put back our temp to our stack so to make sure it is not left out of other possible decodings.
                stack.append(temp)

        # we retunr our stack after we finished iterating and decoding it
        return ("".join(stack))