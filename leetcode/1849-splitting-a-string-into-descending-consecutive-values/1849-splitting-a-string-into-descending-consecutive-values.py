class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        
        def backtrack(index: int, prev_val: int) -> bool:
            if index == n:
                return True

            for j in range(index, n):
                current_val = int(s[index:j+1])
                
                if current_val == prev_val - 1:
                    if backtrack(j + 1, current_val):
                        return True
                
                elif current_val >= prev_val:
                    break
                    
            return False


        for i in range(n - 1):
            first_val = int(s[:i+1])
            if backtrack(i + 1, first_val):
                return True
                
        return False