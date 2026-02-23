"""
- The question: we are given a list of integers and tasked to group all non zero elements before all the zero elements while keeping theire relative order to eachother.
- Solution:
    - to solve the problem we can use two diffrent techniques.
    - the first one is to iterate over the given list and if the current element is non zero element we append it to our temp list.
        - else if it is zero we add 1 to zero counter variable.
        - after completing the iteration we append zero counter amount of zeros to our temp list and we set input list nums equal to our temp since we wont be rturning.
        - this approach is technicaly O(n) both space and time, but we are using extra space to store temp value. and we have additional oprations that cost time. but we can optimize the approach to O(n) time and O(1) space complexity and reduce the extra oprations.
    - the second approach uses two pointers. one seeker and one holder.
        - what we do is we start our holder at index 0 and seeker at 1.
        - then we check if the element in holder index is non zero or not.
        - if it is zero, we check if the seeker is pointing to non zero element.
        - if both conditions are satisfied we swap the elements on the two pointers and increment both elements.
        - else if the seeker is pointing on zero we increment it until we find non zero number or reach our end of list.
        - this approach solves the problem in place and runs on O(n) time.
-  Time and Space complexity:
    - Time = O(n), n = len(nums), for both approachs
    - space = O(1), for two pointer and O(n) for using temp array 
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
   
        """
        twoPtr(nums)

# using temprory array 
def tempArry(nums):
    temp = []
    zero_count = 0

    for num in nums:
        if num != 0:
            temp.append(num)
        else:
            zero_count += 1
    
    for i in range(zero_count):
        temp.append(0)
    
    # modifies the global nums list 
    nums[:] = temp


# using two pointers
def twoPtr(nums):
    hold = 0

    for seker in range(1,len(nums)):
        if nums[hold] == 0 and nums[seker]:
            nums[hold], nums[seker] = nums[seker], nums[hold]
            hold +=1

        elif nums[hold] != 0:
            hold +=1
            