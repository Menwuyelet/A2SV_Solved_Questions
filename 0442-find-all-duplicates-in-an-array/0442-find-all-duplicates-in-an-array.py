"""
- The question: given a list of numbers we are tasked to find numbers that appear twice on the list.
               - the solution should run on O(n) time and O(1) space additional to the space used to store the output.
- Solution:
    - we can solve this problem by iterating through the list one time and store their count.
    - to store their count we can use two methods, 
    1, using dict to store count of every number and as we count appendig the numbers with duplicates to ans list.
    2, using sign flip technique to flag already visited number. sign flip means when we visit a number we go to the index visited num - 1 and 
       - change the sign of that number as flag. this gurantees the when ever we visit a number we can check if it is visited or not. this technique is 
         feasable because of the constraint saying the numbers are in range of 1 to n. so we can map every number to valid index by just subtracting 1 
         since lists are 0 indexed.
-  Time and Space complexity:
    - Time =  both techniques O(n)
    - space = using dict: O(n), using sign flip: O(1)
"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return use_sign(nums)



# using dictionary O(n) time and O(n) space
def use_dict(nums):
    count = {"two": []}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] > 1:
            count["two"].append(num)
            count.pop(num)
    return count["two"]

# using sign flip 
def use_sign(nums):
    ans = []
    for x in nums:
        index = abs(x) - 1
        if nums[index] < 0:
            ans.append(abs(x))
        nums[index] = -nums[index]
    return ans