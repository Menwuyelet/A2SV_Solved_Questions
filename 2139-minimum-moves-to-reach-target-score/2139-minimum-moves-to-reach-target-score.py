"""
- The question: we are given a target number and a maximum multiplication we can do and tasked to find the smallest number of oprations we could do to get the target starting from 1.
                - we can do two opratinos, 1, add 1 to the current num
                                           2, multiply the current num by 2 but only if we have positive multiplication left.
- Solution:
    - the obvious way to minimize the oprations is to use as much as posible multiplication.
    - but we are limited by the maxdoubles so we will multiply the number as much as we can.
    - and add 1s at the end to make the target.
    - to do that we will use division. 
    - we check if the current target is divisible by two, if so we add 1 to our move and divide it.
    - else we add 1 to our move as well as to our reminder and flor divide it.
    - we do that untile we hit 1 or finish our mac doubles.
    - if we finish our max doulbles we then take the moves, reminders and the reminiging number and add them together and subtract 1 to get our minimum move.
-  Time and Space complexity:
    - Time = O(min(log n, log m)), n = target, m = maxDouble
    - space = O(1), 
"""

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if not maxDoubles:
            return target - 1

        reminder = 0
        count = 0
        while maxDoubles and target != 1:
            
            # we check if the current target is divisible by two and dont need addition
            if target % 2 == 0:
                target //= 2
                count += 1
            
            else:
                target //= 2
                count += 1
                reminder += 1

            maxDoubles -= 1

        # we add the remaining number if we are not already at 1
        if target != 1:
            count += target - 1 

        # we return the reminders(add oprations) and multiplication opration counts.
        return reminder + count 