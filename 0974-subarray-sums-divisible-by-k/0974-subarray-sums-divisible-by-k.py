"""
- The question: we are given a list of integers and k, and tasked to find the number of the subarrays that have the sum divided by k.
- Solution:
    - the problem is a subarray with sum divisible by k pattern.
    - so we just implement that algorithm.
    - the algorithm uses runing prefix sum to track the sum of the sub array.
    - to find the sub arrays with a sum divisible by k, we count the reminders at each sub arry.
    - and we add the amount a reminder occured to our answer as it tells us that when two indexes have the same prefix sum mode it tell us that the sub array between the two indexes have the mode equal to 0 so divisible by k.
    - after we count in that way we return the ans.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(n)
"""

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        running_prefix_sum = 0

        count = defaultdict(int)
        count[0] = 1

        ans = 0

        # we biuld the runing prefix sum and check its mod to determine if it have a subb array that meets the requirment.
        for num in nums:
            running_prefix_sum += num
            mod = running_prefix_sum % k

            ans += count[mod]

            count[mod] += 1
        
        return ans
    
