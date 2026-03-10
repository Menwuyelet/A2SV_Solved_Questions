class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for chr in logs:
            if chr == "../" or chr == "./":
                if chr == "./":
                    continue
                    
                if stack:
                    stack.pop()

            else:
                stack.append(chr)
        
        return len(stack)