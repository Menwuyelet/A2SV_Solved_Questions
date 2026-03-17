"""
- The question: we are given number x and number n and tasked to return x^n.
- Solution:
    - we could just used pow() method and be done with this problem.
    - but the reason we are tasked to do this is to impliment our oun function using recursion or bit manipulation.
    - we use recursion to solve this problem.
    - the brute force would be to multiply x n times.
    - but this will lead us to TLE.
    - to solve this we could use a mathimatical fact such x^n = x^n/2 * x^n/2 for all n even. and x^n-1 * x to all n odds.
    - so we us this fact to calculate the answer recursively.
    - we first pass the x and n and in our function we check if n is odd or even.
    - if even we call the function again by passing x and n/2, else we call the function passing x, n//2 and we store the returned value on temp.
    - on the return part we return temp * temp if n is even, else temp * temp * x if n is odd.
    - our base case is if n == 0 we return 1.
    - and thats it.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(n), 
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # spacial case in n is lessthan 0
        if n < 0:
            return 1 / self.base(x, -n)
        
        return self.base(x, n)
    
    def base(self, x, n):
        if n == 0:
            return 1

        # we store the value returned from the next call function
        half = self.base(x, n // 2)
        
        # after we recive a value from the next function call we need to return a value to the previous function call
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

        