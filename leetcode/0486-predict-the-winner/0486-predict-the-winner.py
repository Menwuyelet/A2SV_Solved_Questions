"""
- The question: we are given a list of integers and we are playing a picking game taking turns with our freind and we both are playing optimally to win and our goal is to determine if we can win it or not.
- Solution:
    - this problem seems like a greedy problem but if we use a greedy solution we will fail.
    - to solve this problem we can use dp technique by checking every possible choice we can check.
    - to keep score we dont need to keep both scores rather we can track the diffrence and take every time a choice that gives the maximum diffrence.
    - at the end if we have 0 or positive as our diffrence we return True as we could win it else False.
-  Time and Space complexity:
    - Time = O(n^2), n = len(nums)
    - space = O(n^2), 
"""

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        ans = predict(nums, 0, len(nums) - 1)

        return True if ans >= 0 else False

# we use a function to call it recursivly
def predict(nums, l, r):

    # our base case is that when we are left with only one choice we take it
    if l == r:
        return nums[l]
    
    # else we have multiple choices we calculate both choices and return the max to the func who called it.
    left = nums[l] - predict(nums, l + 1, r)
    right = nums[r] - predict(nums, l, r - 1)

    return max(left, right)