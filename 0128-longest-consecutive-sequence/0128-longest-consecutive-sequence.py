class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set(nums)
        seen = set()
        count = 0
        for i in nums:
            temp = 0
            if i - 1 not in visited and i not in seen:
                seen.add(i)
                x = i
                while x in visited:
                    temp += 1
                    x+=1
            count = max(count, temp)    
        return(count)
