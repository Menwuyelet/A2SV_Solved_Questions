"""
- The question: we are given a list of numbers and tasked to return the numbers that yield the maximum sum of difference while having the smallest elements.
- Solution:
    - we notice that for a nums a < b and c > b, the |a - b| + |b - c| + |a - c| gives the same answer as |a - c| 
    - we see that the second gives the same result with fewer elements.
    - so what we are going to do is the first and last numbers will be always included, and for the numbers in the middle we check that if they are local minimum or maximum
    - if so we add them to our ans else we jum them
-  Time and Space complexity:
    - Time => O(n), len(nums)
    - space => O(n)
"""

for _ in range(int(input())):
    n = int(input())
    nums = [int(num) for num in input().split()]

    ans = []

    for i in range(n):
        if i == 0 or i == n-1:
            ans.append(nums[i])
        else:
            if (nums[i] > nums[i+1] and nums[i] > nums[i-1]) or (nums[i] < nums[i+1] and nums[i] < nums[i-1]):
                ans.append(nums[i])
    
    print(len(ans))
    print(*ans)