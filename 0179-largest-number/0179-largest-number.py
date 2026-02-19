class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        str_nums = list(map(str, nums))
        sorted_nums = sorted(str_nums, key=cmp_to_key(compare), reverse=True)
        
        return str(int("".join(sorted_nums)))
        
        
        
def compare(a, b):
    a = str(a)
    b = str(b)
    
    i = 0
    while True:
        # get digit or last digit if out of range
        if a + b > b + a:
            return 1
        else:
            return -1