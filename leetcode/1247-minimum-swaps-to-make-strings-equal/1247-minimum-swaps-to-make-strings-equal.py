"""
- The question: given two strings s1, s2 consist of only x and y, we are tasked to find out the minimum number of swaps to make the two strings equal. if it is imposible return 1.
- Solution:
    - since only there is two missmatchs, when s1[i] == x and s2[i] == y or s1[i] == y and s2[i] == x we just need to count the missmatchs.
    - two missmatch of each type cost 1 swap to fix.
    - two one each type of missmatch costs 2 swap to fix.
    - one additional case is if the sum of each missmatch present on the strings is odd, we cant fix them so we pring -1
-  Time and Space complexity:
    - Time = O(n), n = len(s1)
    - space = O(1), 
"""
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 0
        yx = 0
        
        for a, b in zip(s1, s2):
            if a == 'x' and b == 'y':
                xy += 1
            elif a == 'y' and b == 'x':
                yx += 1
                
        # if sum of missmatchs is odd we can fix them by swaping
        if (xy + yx) % 2 != 0:
            return -1
        
        return (xy // 2) + (yx // 2) + 2 * (xy % 2)
