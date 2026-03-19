"""
- The question: we are given a linked list and tasked to to partition it in tow parts. the first one contains elements with value smaller than the given value (x) teh second one contains nodes with value greater or equal to the given value (x)
- Solution:
    - so to do this we can use two linked lists one to store the smaller ones and one to store the larger ones.
    - after that we iterate through the given linked list and assign nodes to one of the lists based on theire value.
    - after we finish that we join the two lists and we make sure that the last element of the larger list points to none.
    - that is because if we leave it as it is lets say for given list [1,2,3,9,5,7,8] and x = 7, our last element for larger list as well as our partitiond list will be 9. 
    - and as you can see 9 was originaly pointing to 5 and after partition it will also be pointing to 5 that creates circular loop and make the memory limit.
    - so we set the last element of the partitiond list or the last node of the larger list point to none.
-  Time and Space complexity:
    - Time = O(n), n = length of the given linked list
    - space = O(n), 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_list = ListNode(0)
        larger_list = ListNode(0)

        curr_small = smaller_list
        curr_large = larger_list

        curr = head

        while curr:
            # if our current value is greater or equal to the value given we add it to the larger list 
            if curr.val >= x:
                curr_large.next = curr
                curr_large = curr_large.next
            
            # if our current value is less than value given we addit to the smallest list
            else:
                curr_small.next = curr
                curr_small = curr_small.next

            curr = curr.next
        
        # we set the last of the larger_list to none to avoid pointing to the old values of the last node pointing to   
        curr_large.next = None
        curr_small.next = larger_list.next

        return smaller_list.next
        