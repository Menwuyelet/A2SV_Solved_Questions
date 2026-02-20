"""
- The question: given a list of n integers representing the number of problems in the ith contest, we are tasked to find the maximum number of days polycrap can train for, given that on the ith day he can only train for a contest with at least i problems.
    if the number of problems in the contest is less than i, he can't train that contes for that day, but if it is greater than to i he trains on i problems and let the rest of the problems be left.
- Solution:
    - we can sort the list of contests and then iterate through it, if the number of problems in the contest is greater than or equal to the current day we can train for that contest and move to the next day, 
    - else we can't train for that contest and we move to the next contest.
    - if we reach the end of the list of contests, we stop and the number of days we trained for is our answer.

-  Time and Space complexity:
    - Time => O(n log n) due to sorting the list of contests
    - space = O(1), we only use a constant amount of space to store the ans integer.
"""

n = int(input())
contests = list(map(int, input().split()))
contests.sort()
ans = 0
idx = 1
for i in range(n):
    # if the number of problems in the contest is greater than or equal to the current day we can train for that contest and move to the next day,
    if contests[i] >= idx:
        ans += 1
        idx += 1
    
print(ans)