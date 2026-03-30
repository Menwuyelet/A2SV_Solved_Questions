"""
- The question: we are given a list and list of queries and tasked to return the maximum sum of accros these queries but we should change the permituation of the given list to maximize the result.
- Solution:
    - so what we need to do is that we should sort the list in order that the maximum number from the list gets the plce wehere there is a max query count.
    - to do that we first need to find the query count of each index. to do that we can use prefix sum to do range opration on a list of all zeros and find its prefix sum to obtain the indexes query count.
    - after that we allocate the max number form the list to the max query count holder index.
    - to do that we just sort both the prefix sum and the number and multiply each element by element and add tehem to our answer that gives us the max sum we could ever have.
    - finally we mod our answer by (10**9 + 7) as the problem states it
-  Time and Space complexity:
    - Time = O(n log n), n = len(nums), due to the sorting
    - space = O(n), 
"""

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        # we first do the range queries 
        request_sum = [0] * (len(nums) + 1)
        for request in requests:
            request_sum[request[0]] += 1
            request_sum[request[1]+1] -= 1

        # after doing the range opration we calculate the prefix sum to find the actual frequency of query
        request_sum.pop()
        for i in range(1, len(request_sum)):
            request_sum[i] = request_sum[i] + request_sum[i-1]

        # sort both lists and calculate the answer by myltiplying each element with one another and adding it to our ans
        request_sum.sort()
        nums.sort()

        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            ans += nums[i] * request_sum[i]

        # we mod the ans by the given number to get the expected ans
        return ans % (10**9 + 7)