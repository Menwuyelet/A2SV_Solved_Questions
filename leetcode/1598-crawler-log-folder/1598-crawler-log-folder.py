"""
- The question: we are given a logs of the directories visited and tasked to find out how many moves are required to get back to the home directory. the given lods contain directory names and file traversing commands.
- Solution:
    - to solve this we can count the number of file names and the number of backward moves the log contains and subtract them to each other and we are done.
    - the other way is to use stack and do the same thing but one log at a time.
    - we iterate through the logs and when the given log is a directory name we apped it to our stack.
    - if it is backward move command we pop from our stack, else if it is a comand to remain at the current directory we just do nothing for that iteration.
    - after we finish we return the len of our stack.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(n), 
"""

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for chr in logs:
            if chr == "../" or chr == "./":
                
                # if the current comand is to stay in the current directory we just skip this iteration
                if chr == "./":
                    continue
                
                # we only pop from the stack if it is not empty
                if stack:
                    stack.pop()
            
            # we add it to our stack if it is not a command to go back or stay there
            else:
                stack.append(chr)
        
        return len(stack)