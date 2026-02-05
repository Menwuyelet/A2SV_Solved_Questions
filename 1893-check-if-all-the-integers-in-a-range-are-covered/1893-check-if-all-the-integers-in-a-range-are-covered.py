class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        ptr = 0
        ans = [False for i in range(60)]
        leftPtr = left
        x = 0
        for l, r in ranges:
            for x in range(l, r+1):
                ans[x] = True
        
        for x in range(left, right+1):
            if not ans[x]:
                return False
        return True
            