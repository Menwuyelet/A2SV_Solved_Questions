"""
- The question: we are given a list containing only numbers 0 - 2 and tasked to sort them in place without using sort() method.
- Solution:
    - so this problem seems hard at first but the fact that there are only three type of numbers always makes it easy.
    - since the type of numbers is limited to the given three we could just count the times each appear and modify the given list acordingly.
    - that is, we count how many times lets say 0 appears and we update the elements of nums from idx 0 to the frequency of 0 to value 0, and we do the same for 1 after we finish 0 and we do the same for 2 after we finish for 1.
    - that is it
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(n), 
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # we count the frequencies
        count = Counter(nums)

        # we use an idx variable to sort the nums in modified order
        index = 0

        # we iterate over the three posible values and check theire frequency and iterate over that frequency and modify our nums in place
        for key in [0,1,2]:
            for j in range(count[key]):
                nums[index] = key
                index += 1