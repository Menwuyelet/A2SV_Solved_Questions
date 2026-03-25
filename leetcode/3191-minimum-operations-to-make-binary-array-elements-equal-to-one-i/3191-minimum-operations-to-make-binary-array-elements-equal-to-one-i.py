"""
- The question: we are given a list of binary numbers and tasked to convert all zeros in to ones.
                - but we can only perform one type of opration, we can only take three consiquetive elements and flip them.
                - and we must find if it is posible to obtain all 1s doing only these opration if so return the minimum nuber else -1
- Solution:
    - this is basically a sliding window problem with a fixed window of size 3.
    - we iterate through the list with this window and if we find a zoro on our left ptr we flip all the elements in our window and add 1 to our count.
    - else we continue until we hit left ptr equal to len(nums) - 2.
    - after that even if we find a 0 we couldnt change it so our answer will be -1.
    - after we finish the iteration we check if there are any zeros in the nums[k:] part if so we return -1 since we cant convert them else we return the count of oprations we did.

-  Time and Space complexity:
    - Time = O(n * 3) = O(n), n = len(nums)
    - space = O(1), 
"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        left = 0
        count = 0

        # we check if the given nums have length of 3 and if it contains both 1 and zero, if so we couldnt convert it so se return -1
        if len(nums) == 3 and 0 in nums and 1 in nums:
            return -1

        # we iterate over the list with the given window of 3 and convert it
        for right in range(2, len(nums)):

            # if we find 0 we iterate over the window and flip all the elements and add 1 to our counter.
            if nums[left] == 0:

                for i in range(left, left + 3):

                    if nums[i] == 0:
                        nums[i] = 1
                    else:
                        nums[i] = 0

                count += 1
        
            left += 1
        
        # after completing the iteration we check for the remaining part of the list since we stop the iteration at len(nums) - 2 
        if 0 in nums[left:]:
            return -1
        
        # if we pass the check we return our count as our answer.
        return count
