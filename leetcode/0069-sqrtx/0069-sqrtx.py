"""
- The question: we are given an integer and we are tasked to return its square root, but we can't use exponential functions.
- Solution:
    - we just can solve this problem using binary serach and trying every value as possible answer.
    - we first make our high to our x and low to 1 and use binary search to split it in to tow halves and check if the middle is our answer or not.
    - if so we just simply return it else
    - we check if our answer is between our mid and mid + 1 if so we return our mid
    - but if our mid generates larger value we make our high our mid
    - but if our mid generates smaller value we make our low to our mid then do the same thing.
- Time and Space complexity:
    - Time = O(log n), n = len(nums)
    - space = O(1), 
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        
        left = 1
        right = x

        # we handle edge case when x = 0
        if x == 0:
            return 0


        while left <= right:
            
            # we calculate our mid 
            mid_num = (left + right) // 2

            # check if our mid is the perfect answer
            if mid_num * mid_num == x:
                return int(mid_num)

            # check if our answer is between our mid and mid + 1
            elif mid_num * mid_num < x and (mid_num + 1) * (mid_num + 1) > x:
                return mid_num

            # we update our mid based on what it generates
            elif mid_num * mid_num < x:
                left = mid_num

            elif (mid_num * mid_num) > x:
                right = mid_num
            
            
        

             
