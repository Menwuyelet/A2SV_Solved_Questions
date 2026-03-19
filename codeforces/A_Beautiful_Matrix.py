"""
- The question: given a 5*5 matrix with all elements are 0 except one element is 1, we are tasked to find the minimum number of moves to move the 1 to the center of the matrix. we can move the 1 up, down, left or right.
- Solution:
    - we can iterate over the matrix and find the position of the 1,
    - then we can calculate the distance between the position of the 1 and the center of the matrix (3,3) and that will be our answer.
-  Time and Space complexity:
    - Time => O(1), since the matrix is fixed size (5*5)
    - space = O(1)
"""

count = 0
ans = 0
for _ in range(5):
    nums = [int(num) for num in input().split()]
    count += 1
    if 1 in nums:
        ans = abs(3 - count) + abs(3 - (nums.index(1) + 1))
        break
print(ans)
