class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
    
        ranges_set = set()
        for start, end in ranges:
            for i in range(start, end+1):
                ranges_set.add(i)
        
        for num in range(left, right+1):
            if num not in ranges_set:
                return False
        return True