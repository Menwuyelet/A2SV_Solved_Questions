"""
- The question: we are given a list of numbers and an integer n and tasked to patch the array until all the numbers in range n can be found from the sum of any numbers.
- Solution:
    - so the first and brute force approach would be to generate all the possible sums and add the numbers we cant get from these sums, but that would cause TLE
    - so we need to find O(n) solution and that would be to keep track of the comulative sum until now and compare the current number
    - if the current number is lesthan or equal to our cumulative sum we just add it to our comulative sum since it is garantied we can obtain it from some sum.
    - but if it is larger we add 1 to our answer and add the current + 1 to our current to increment it by 1
    - after we are done with our iteration we return answer.
-  Time and Space complexity:
    - Time = O(n), n = given n
    - space = O(1)), 
"""

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        curr_sum = 0
        index = 0
        count = 0
        
        # we iterate until our current summ hits our n
        while curr_sum < n:

            # we check if the current sum + 1 is larger than our current number, if so it can be found form some sum
            if index < len(nums) and nums[index] <= curr_sum + 1:
                curr_sum += nums[index]
                index += 1
            
            # else we need to add the current sum + 1 to our list and increment our count
            else:
                curr_sum += curr_sum + 1
                count += 1
        
        # after reaching n we return our count as minimum additions of elements
        return count
 

        
                
                
