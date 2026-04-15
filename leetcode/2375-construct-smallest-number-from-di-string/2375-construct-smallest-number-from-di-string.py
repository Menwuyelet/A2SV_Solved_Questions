"""
- The question: we are given a string of patterns containing only letters "I" and "D" and these letters are comands to be performed. we are tasked to generate smallest posiible number containing only 1 - 9 following:
                - If pattern[i] == 'I', then num[i] < num[i + 1].
                - If pattern[i] == 'D', then num[i] > num[i + 1].
- Solution:
    - we just iterate and append numbers considering the current chr.
    - to handle decreasing chrs we use stack.
    - we iterate over 0 to len(patterns) + 1 and append i + 1 to our stack and if the char is "I" we flush the stack and reverse extend it to our answer.
    - if it is "D" we just move to the next iteration.

-  Time and Space complexity:
    - Time = O(n), n = len(pattern)
    - space = O(n), 
"""


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []

        res = []

        for i in range(len(pattern)+1):
            
            # we add i + 1 to our stack
            stack.append(str(i + 1))

            # if our chr is "I" or we are at the end of the iteration we flush the stack and extend it to our res
            if i == len(pattern) or pattern[i] == "I":
                res.extend(stack[::-1])
                stack.clear()
            
        return "".join(res)



