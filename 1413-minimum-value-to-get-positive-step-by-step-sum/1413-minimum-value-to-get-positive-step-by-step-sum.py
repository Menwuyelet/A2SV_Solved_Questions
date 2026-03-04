"""
- The question: we are given a list of integers with value of both -ve and +ve. we are tasked the minimum posible number that we can take and we calculate the sum of each integer in the list and we wont get a sum less than 1.
                - [-3,2,-3,4,2], we take 3 as our initial value we add it to first element -3 and we get 0 so we cant take 3 as our start value.
                - we take 4, we add it to the first element we get 1, and we take that and add it to the second 2 element and we get 3.
                - we take 3 and we add it to the third element -3 and we get 0 so we also cant take 4 as starting value.
                - but if we take 5 we gurantee we will never hit a sum below 1 going forward like this.
- Solution:
    - so what we going to do is that we calculate the runing sum of the given array and we take the minimum value.
    - if the minimum value is 0 or greater we take 1 as our start and we will be fine.
    - but if it is negative number we take the absolute value of that number and add 1 to it and thats our answer and starting value to guarantee we never hit bellow 1.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(n), 
"""
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        runing_sum = 0
        min_value = float('inf')

        # caluculate the runing sum 
        for num in nums:
            runing_sum += num
            min_value = min(min_value, runing_sum)
        
        if min_value >= 0:
            return 1
        
        return abs(min_value) + 1
        
    
