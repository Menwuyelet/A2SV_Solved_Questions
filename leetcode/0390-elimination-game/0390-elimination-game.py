"""
- The question: given integer n, we are tasked to perform two oprations repeatdly on a list of 1 to n (inclusive) until there is only one number remainig
                - the oprations are: remove every other element going from left to right and do the same but in reverse from right to left.
- Solution:
    - the brute force solution of this problem would be to iterate back and forth and remove the elements along the way.
    - but this is not optimal for several reasons like removing from the first index, going back and forth and so on.
    - so instead of doing the acrual removal or simulation we could use a mathimatical relation to solve the problem.
    - that relation is the problem size is halved every time we change direction. and in the first time going from left to right we remove all the odd numbers so the list will be consisting of only even numbers.
    - so the numbers in the list can be represented as 2 * (range(1, n//2)).
    - that is it after this, this patern will be repeated the only diffrent is that we change direction.
    - to acomodate that we can reverse it by, let f(n) be result of a left to right pass on list length n so  n + 1 - f(n) will be the reversed version of that.
    - and let g(n) be (n + 1 - f(n)) so for g(n//2) = (n//2 + 1 - f(n//2))
    - the whole equation will become 2 * g(n//2) = 2 * (n//2 + 1 - remove(n//2))
-  Time and Space complexity:
    - Time => O(log n), n = n
    - space = O(log n), due to call stack
"""
class Solution:
    def lastRemaining(self, n: int) -> int:

        def remove(n):

            # our base case 
            if n == 1:
                return 1
            
            
            return 2 * (n//2 + 1 - remove(n//2))
        
        return remove(n)