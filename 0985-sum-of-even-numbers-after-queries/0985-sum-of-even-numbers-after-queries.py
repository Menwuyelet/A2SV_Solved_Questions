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
                # print(nums[query[1]])
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
