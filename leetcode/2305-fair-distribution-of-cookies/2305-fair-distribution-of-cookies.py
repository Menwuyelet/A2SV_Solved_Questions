class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # children array stores the total cookies each of the k children has
        children = [0] * k
        self.ans = float('inf')
        
        def backtrack(idx):
            # All cookie bags distributed
            if idx == len(cookies):
                self.ans = min(self.ans, max(children))
                return
            
            # If the current max already exceeds our best ans, stop
            if max(children) >= self.ans:
                return
            
            # Try giving the current bag (idx) to each of the k children
            for i in range(k):
                children[i] += cookies[idx]
                backtrack(idx + 1)
                children[i] -= cookies[idx] 
                
                # If child i had 0 cookies before this, giving the bag to child i+1 would be a redundant state.
                if children[i] == 0:
                    break
        
        # Sorting cookies in descending order helps pruning trigger earlier
        cookies.sort(reverse=True)
        backtrack(0)
        return self.ans