"""
- The question: given an integer we are tasked if there are two positive integers that give the given number when raised by two and summed.
- Solution:
    - so this problem requires us to find two numbers that are squared and summed and give our target.
    - from mathimatical observasion we can see that we only need to scan for numbers from 0 to square root of our given number.
    - that is because the max and min numbers that give the number when squared and added are 0 and square root of the number.
    - if we pass the square root we mathimaticaly cant find a number that will give us our target.
    - so we first find the square root of our given number and if it is perfect nuber we return True auto because we found 0 and the square root of the number.
    - else if it is not perfect square we create a list of numbers from zero to the square root and use colliding pointers to find the two numbers.
    - when we find the two numbers we return true and we are done.
    - but if the two pointers pass eachother we stop and return false.
-  Time and Space complexity:
    - Time = O(n), n = square root (c)
    - space = O(1), 
"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # since we only need to check the numbers up to square root of c by mathimatical fac
        bound_num = int(math.sqrt(c))

        left_ptr = 0
        right_ptr = bound_num

        # if our num is perfect square we return true
        if isPerfectSquare(bound_num, c):
            return True

        while left_ptr <= right_ptr:
            # if we find the two numbers we return true and no need to continue
            if (left_ptr * left_ptr) + (right_ptr * right_ptr) == c:
                return(True)
            
            # if the two numbers produce larger we decrement the number by decrimenting our right ptr
            elif (left_ptr * left_ptr) + (right_ptr * right_ptr) > c:
                right_ptr -= 1

            # if the two numbers produce smaller we increment the number by decrimenting our left ptr
            else:
                left_ptr += 1

        return(False)

    
def isPerfectSquare(n, c):
    return n*n == c