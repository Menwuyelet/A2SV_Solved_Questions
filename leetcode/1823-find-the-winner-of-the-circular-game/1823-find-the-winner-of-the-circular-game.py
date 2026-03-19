class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        def find(n):
            if n == 1:
                return 0

            return (find(n - 1) + k) % n
        
        return find(n) + 1