"""
- The question: we are given a string containing parenthesis and english letters and tasked to generate all posible valid parenthesis with minimum removal of parenthesis.
- Solution:
    - so to solve this problem we should consider the number of removals we make. we want to minimize it.
    - so to achive this we check each possible removals to see if they generate valid parenthesis.
    - we start with the original string and check if it is valid if so we just append it and return it.
    - if not we generate all possible strings obtaind when we remove only one chr from the string and check if that generates any valid string if so we add all the valid strings and return them. else we continue to remove 2 elements and do it over again.
    - we continue removing until we find a valid generating removal level or we reach the limit of removal.
    - this solution is not backtracking solution it is exploring removal level by level.
-  Time and Space complexity:
    - Time = O(2^n)
    - space = O(2^n), 
"""

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        # we use set to avoid checking already checked strings to optimize it 
        res = []
        visited = set([s])
        queue = deque([s])
        found = False
        
        # we iterate until our qeue is null
        while queue:
            curr = queue.popleft()
            
            # we check if the current string is valid if so append it to our res and flag the found to True to avoid furthur removal
            if isValid(curr):
                res.append(curr)
                found = True
            
            # if found we don not need to go furthur in the removal because we have the optimal removal level that generates valid strings
            if found:
                continue
            
            # if the current removal wont generate any valid string we continue our removal of the next chr
            for i in range(len(curr)):

                # we only remove it if it is not letter
                if curr[i] not in '()':
                    continue
                
                # we generate our next string by removing one chr
                nxt = curr[:i] + curr[i+1:]
                
                # we check if we have processed this string before if so we won't do it again
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
        

        return res   

# hellper function to check if the curren string is valid or not
def isValid(string):
        count = 0
        for ch in string:
            if ch == '(':
                count += 1
            elif ch == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0