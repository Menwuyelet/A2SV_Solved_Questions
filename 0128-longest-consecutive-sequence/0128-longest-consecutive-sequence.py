"""
- The question: we are given a list of integers and tasked to find the longest consecutive elements. we should solve this by O(n)
- Solution:
    - we could solve this problem by sorting it and iterating through it and count the max sequence.
    - but sorting have O(n log n) so we cant use sorting.
    - so to solve this with O(n) we should come up with a solution that only iterates through the list once.
    - we could use set to track the list and iterate through the list and start the sequenc only when curr_num - 1 is not in the list.
    - this guarantees that we wouldnt process already proccesd sequence because if curr_num - 1 is in the list and we start the sequence from curr_num, we are already 1 digit down and wouldn't be max.
    - after we verify we havn't processed the curr_num we start the sequence count by starting form the curr_num and checking every number every time we incrementing by 1.
    - and when we can't find the curr_num + 1 thats when our sequence breaks and we can compare the current sequence with the current max and store it.
    - to make it more optimal we can add additional seen variable that will elminate starting the same count for duplicate numbers.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(n), 
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        seen = set()
        max_sequence = 0

        for curr_num in nums:
            temp = 0

            # this checkes if we already procecced the number.
            if curr_num - 1 not in nums_set and curr_num not in seen:
                # to avoide checking the sequence for duplicate numbers
                seen.add(curr_num)
                
                next_num = curr_num

                # this initiates the sequence count
                while next_num in nums_set:
                    temp += 1
                    next_num += 1
        
            max_sequence = max(max_sequence, temp)  

        return(max_sequence)
