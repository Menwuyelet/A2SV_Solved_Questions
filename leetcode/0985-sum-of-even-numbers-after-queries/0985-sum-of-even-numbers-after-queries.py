"""
- The question: given a list of numvbers and list of queries we are tasked to list out the sum of all the even numbers after performing each query.
- Solution:
    - the brute force approach to this solution would be iterating throut the queries and updating the numbers and after that computing the sum each time.
    - but this will take time. so to avoid computing the sum each time we can use running sum and updating it as we perform the queries.
    - when doing the queries we need to think about 4 possiblities.
    - 1, the number being updated is an even number and after the computaion it will also be an even number,
    - 2, the number being updated is an odd number but after the update it will be even,
    - 3, the number being updated is an even number but after the update it will be odd,
    - 4, the number being updated is an odd number and after the update it will stay odd.
    - for the first condition we add the addition number given in the query to the current sum,
    - for the second we add the entire number to the current number,
    - for the third we subtract the number from the current sum as it is being an odd
    - for the fourth we just append the current sum to our ans and update the number.
-  Time and Space complexity:
    - Time = O(n + m), where n = len(nums), m = len(queries)
    - space = O(m),
"""



class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        curr_sum = sum(num for num in nums if num % 2 == 0)
        ans = []
        for query in queries:
            if nums[query[1]] % 2 == 0 and (nums[query[1]] + query[0]) % 2 == 0:
                nums[query[1]] = nums[query[1]] + query[0]
                curr_sum += query[0]
                ans.append(curr_sum)
            elif nums[query[1]] % 2 != 0 and (nums[query[1]] + query[0]) % 2 == 0:
                nums[query[1]] = nums[query[1]] + query[0]
                curr_sum += nums[query[1]]
                ans.append(curr_sum)
            elif nums[query[1]] % 2 == 0 and (nums[query[1]] + query[0]) % 2 != 0:
                curr_sum -= nums[query[1]]
                nums[query[1]] = nums[query[1]] + query[0]
                ans.append(curr_sum)
            else:
                nums[query[1]] = nums[query[1]] + query[0]
                ans.append(curr_sum)
        if ans: 
            return ans
        return [0] 
