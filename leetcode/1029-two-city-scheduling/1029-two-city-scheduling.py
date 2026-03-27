"""
- The question: we are given a list of lists each list containing 2 values, value at ith index represent a cost of making the ith person go to city a and city b repectivly.
                - and we are tasked the minimum total cost when exactly half people goes to city a and city b spliting them equally to the two cities.
    
- Solution:
    - so this questions is a litle bit triky and the approach might not come mind fast.
    - the approach we use is greedy but greedy on the diffrnece between the costs of the two cities for each person.
    - so first we biuld a list containing the the difrence between the cost of taking the ith person to city a and city b allong side with its index [(cost(city a) - cost(city b), index]).
    - then we sort that list by its first element and we iterate over it checking if we reached or passed the midle of the original list.
    - if we are not yet to reach or cross we add that person to go to city a, else to city b
    - and that is it we add the costs accordingly and that cost is the minimal posible.
-  Time and Space complexity:
    - Time = O(log n), n = len(nums)
    - space = O(log n), 
"""

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        # we biuld the cost diffrence list 
        cost = []
        for i, value in enumerate(costs):
            cost.append([value[0] - value[1], i])
            
        
        # we sort the cost diffrence list and iterate over it checking if we are yet to cross the midle or not and adding appropriate cost to our answer.
        cost.sort()
        ans = 0
        for i in range(len(costs)):

            # if we are yet to be at the midle we take the cost of first city
            if i < len(costs)/2:
                ans += costs[cost[i][1]][0]
            
            # else we take the cost of the second city
            else:
                ans += costs[cost[i][1]][1]


        return ans
        
        