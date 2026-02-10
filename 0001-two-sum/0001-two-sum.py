class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDic = {}
        for i in range(len(nums)):
            numsDic[nums[i]] = i
        
        for i in range(len(nums)):
            number = target - nums[i]
            if number in numsDic and numsDic[number] != i:
                return(i, numsDic[number])