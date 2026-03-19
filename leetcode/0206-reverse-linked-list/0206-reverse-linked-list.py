"""
- The question: we are given a head of a linked list and we are tasked to reversse it. but the thing is the linked list is singly linked list.
- Solution:
    - so to solve this we just create a new linked list and iterate on the given linked list and add the curr item to the first of our new linked list.
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next = curr.next   
            curr.next = prev 
            prev = curr       
            curr = next        
            
        return prev 
