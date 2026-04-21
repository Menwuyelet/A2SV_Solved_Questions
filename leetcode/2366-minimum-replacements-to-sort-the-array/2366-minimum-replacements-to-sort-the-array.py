"""
- The question: we are given a list of numbers and we are tasked to make sure the list is sorted in increasing order. but the way we sort is that if we have a number that is larger than the number next to it we can split it in to two parts and put these two parts in place of it but we should minimize the number of replacment oprations we perform and return the minimum number of oprations nedded to sort it.
- Solution:
    - so we start at the back of the list and make it the current right which we will use to compare it.
    - we do that because that last number should be the largest number in that list so the list is to be sorted.
    - after that we check each numbers and if there exist a number larger than our current righ we use a formula (math.ceil(current number / current right) - 1) to find the number of splits nedded to replace it with proper numbers.
    - after that we replace our current right to the (current number // (math.ceil(current number/curr_right)))
    - if the current number is lessthan or equal to the current right we simply replace the current right by the current number
    - then we finish our iteration we return the count as it is the minimum number of replacements nedded to make it sorted.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(1)), 
"""

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        curr_right = nums[-1]
        count = 0

        # we iterate backward
        for num in nums[::-1]:
            
            # if our current number is larger than the current right we split it
            if num > curr_right:
                
                # we use base case of the formula to reduce computation
                x = math.ceil(num/curr_right)

                # we find number of replacments nedded 
                count += x - 1

                # we find the new current right number
                curr_right = (num // x)

            # else we simply replace the current right by the current number
            else:
                curr_right = num

        return count