"""
- The question: we are given a list of peoples waight and a limit of what a boat can hold. we are tasked to deterimine the minimum number of bots we need to save all the peoples.
- Solution:
    - the brute force solution would be to iterate over all the peoples waight and try to find a waight that can be added to current weight without exceeding the boat limit.
    - but to do that it will take O(n^2), we can solve the problem using O(n log n) solution.
    - the solution is simple just like two sums we sort the weights and use coliding poiters and check if they exceed the limit or not.
    - if they did we increase our boat count by 1.
    - else we increase our boat count and move our left pointer.
    - in either cases we move our right pointer.
    - after the pointers colide we can return the boat count.
-  Time and Space complexity:
    - Time = O(n log n), n = len(people)
    - space = O(n), 
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left_ptr = 0
        right_ptr = len(people)-1
        boat = 0

        if len(people) == 1:
            return 1

        while left_ptr <= right_ptr:

            # for odd number of people size
            if left_ptr == right_ptr:
                return boat+1

            # if the current set of people are havier than the limit we add 1 to our boat counter
            elif people[left_ptr] + people[right_ptr] > limit:
                boat += 1
           
            else:
                boat += 1
                left_ptr += 1

            right_ptr -= 1

        return boat