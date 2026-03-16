"""
- The question: we are given a list on nums and tasked to return the number that gives us the minimum sum of the differences from each number in the list
- Solution:
    - the problem is generally asking as the median value of the list.
    - so we sort it and return the median value.
-  Time and Space complexity:
    - Time => O(n * log(n)), since we are sorting
    - space = O(n)
"""

n = int(input())
nums = [int(num) for num in input().split()]
nums.sort()

# find the indx of the median value
idx = int((len(nums) / 2) - 1) if len(nums) % 2 == 0 else int(len(nums) // 2)

print(nums[idx])
