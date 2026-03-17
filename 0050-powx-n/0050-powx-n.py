class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.base(x, -n)
        
        return self.base(x, n)
    
    def base(self, x, n):
        if n == 0:
            return 1


        half = self.base(x, n // 2)
        
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

        