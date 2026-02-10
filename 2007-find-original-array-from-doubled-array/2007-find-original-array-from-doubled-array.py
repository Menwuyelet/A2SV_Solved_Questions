"""
- The question: given a list of integer we are tasked to findout if the list is doubled and if so return the original list else return empty list
- Solution:
    - so to solve this we can iterate through the list and check if num*2 is on the list if so we put num in our ans(original list)
    - to check that we can use counter to count available numbers and sort the given list and iterate throu it and checking if both num and num*2 are in the counter we decrement them by 1 and append the num to our ans.
    - if the num is 0 we decrement twice from it since 2*0 = 0
    - after the loop ends we check if the ans is half the length of the given list. if so we return ans else []
-  Time and Space complexity:
    - Time = O(nlog n), due to the sorting 
    - space = O(n)
"""


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # handles the condition where the given list len is not even 
        if len(changed)%2 == 1:
            return []

        counter = Counter(changed)
        changed.sort()
        ans = []

        for num in changed:
            # handles the case where the num is 0
            if num == 0 and (counter[num] > 1):
                counter[num] -= 2
                ans.append(num)
           
            # handles the general case
            elif num != 0 and (counter[num] and counter[num*2]):
                counter[num] -= 1
                counter[num*2] -= 1
                ans.append(num)
        
        if len(ans) == len(changed)//2:
            return ans
        return []