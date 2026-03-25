class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mon_de = deque()
        mon_in = deque()
        third = float('-inf')
        
        for num in nums[::-1]:
        
            if third > num:
                return True

            while mon_de and mon_de[-1] < num:
                third = mon_de.pop()
            mon_de.append(num)
            
        return False
