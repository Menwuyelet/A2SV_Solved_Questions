"""
- The question: we are given a list of nums and we are tasked to return the largest posible integer that is produced by concatnating all the digits in the nums.
- Solution:
    - so we are tasked to retrurn the largest posible so what we do is we compare digits of each number per position of the new number and figure out a permtuation that produces the largest.
    - as n grows the permutuation also grows so we need to find a way with out trying all possible ways.
    - we can use sorting with spatial key function.
    - in that function we compare each two digits and take the arrangement which will result in largest for that local sub problem.
            Ex: [34, 5, 9]
                when sorting what we want is to compare which one  345 or 534 (concatnated 34, 5)
                and we sort our entire nums with that logic.
-  Time and Space complexity:
    - Time = O(n log n), n = len(nums)
    - space = O(n), 
"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key  
        # convert the list of int to list str
        str_nums = list(map(str, nums))
        
        sorted_nums = sorted(str_nums, key=cmp_to_key(compare), reverse=True)
        
        return str(int("".join(sorted_nums)))
        
        
        
def compare(a, b): 
    # check which arrangement results larger num
    if a + b > b + a:
        return 1
    else:
        return -1