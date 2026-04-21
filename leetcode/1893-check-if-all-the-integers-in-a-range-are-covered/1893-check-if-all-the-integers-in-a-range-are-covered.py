class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        set_list = set()

        for i in ranges:
            set_list.update(range(i[0], i[1]+1))

        for i in range(left, right+1):
            if i not in set_list:
                return False
        
        return True