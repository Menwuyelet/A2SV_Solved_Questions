class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if not maxDoubles:
            return target - 1
        

        reminder = 0
        count = 0
        while maxDoubles and target != 1:
            if target % 2 == 0:
                target //= 2
                count += 1
            
            else:
                target //= 2
                count += 1
                reminder += 1
            maxDoubles -= 1

        if target != 1:
            count += target - 1 

        return reminder + count 