"""
- The question: we are given a list of integers and k, and tasked if there exist a giid syb array. 
                - a subarray is good if its length is atleast 2 and sum of its elements is multiple of k
- Solution:
    - the brute force solution for this problem would be to check every sub array with a length of 2 or more.
    - but this approach takes a lot of time.
    - so we look other ways and we actually use prfix sum.
    - what we do is that we track reminder map and prefix_sum.
    - the reminder map is a dictinary where we store the index of the ending of a sub array with its reminder as key.
    - the prefix sum is used to calculate the reminder.
    - then we check if the reminder is obtaind before and check if the current index giving the reminder and the earlier index have a difrent of atleast two.
    - if so we return true. we iterate untile we hit true or we end the list.
    - if we end the list we return false as we havent found a good subarray.

-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(n), 
"""

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
   
        remainder_map = {0: -1}  
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if k != 0:
                remainder = prefix_sum % k
            else:
                remainder = prefix_sum 

            # we check if the reminder is obtaind before and if so we check the length of the subarray that gave us the reminder.
            if remainder in remainder_map:
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                remainder_map[remainder] = i

        return False