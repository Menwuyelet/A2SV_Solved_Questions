"""
- The question: we are given integer n and tasked to find how many good numbers exisist that have a number of digits equal to n.
                - good number is a number that all the even indices of that number is only occupied by even number and all the odd indices are occupied by prime numbers.
- Solution:
    - this is basic counting problem.
    - we use the multiplication rule to determine how many good numbers exist.
    - the problem is to use muptiplication rule we must know the two numbers we multiply.
    - in our case the number of even slots and odd slots.
    - these numbers are determind by deviding the number of digits to two.
    - the other thing is to find the multiplied numbers we need to raise the number of choices we have for that slot by the count of that slot.
    - so for even slots we need to raise 5(number of choice we have to put on even slot) by the number of even slots we have. for odd we have 4.
    - to find the real problem of this question is the number of the slots get bigger and bigger so the raising opration will be so slow for huge numbers of slots.
    - so to solve that we use the fast power function that uses recurstion to find the result of x raise to n for huge numbers.
    - that function uses recurssion to calculate the raise opration.
    - again that function wont be enough since our number will get up to 10^15. so we use modulo opration to decrease it by moding it by 10^9 + 7 in each fast power function calls.
    - then we just multiply the results of the even and odd posible choices and return it.
-  Time and Space complexity:
    - Time = O(log n), n = len(nums)
    - space = O(log n), 
"""

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        # we obtain the choices to use the even numbers
        even = self.fast_pow(5, (n+1)//2, mod)

        # we obtain the choices to use the odd numbers
        odd = self.fast_pow(4, n//2, mod)

        # we calculate the total and return it.
        return (even * odd) % mod


    # we use mod to decrease the huge number to make it the opration faster.
    def fast_pow(self, x, n, mod):
        if n == 0:
            return 1

        # we store the value returned from the next call function
        half = self.fast_pow(x, n // 2, mod)
        
        # after we recive a value from the next function call we need to return a value to the previous function call
        if n % 2 == 0:
            return (half * half) % mod
        else:
            return (half * half * x) % mod