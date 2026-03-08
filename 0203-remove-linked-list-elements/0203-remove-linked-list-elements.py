# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
- The question: we are given a linked list and a value. we are tasked to remove the node with value equal to the given value.
- Solution:
    - this is basic linked list traversal problem we just traverse throug the list and remove the node.
    - to do that we can use dummy node at the begining to be able to remove the frist element as well.
    - we check the value of the next node when we are on the current node and if it satisfies we point the current nods next to the next nods next. 
    - this succsesfully removes the node form the linked list.

-  Time and Space complexity:
    - Time = O(n), n = len of the linked list
    - space = O(1), 
"""

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # we use dummy to enable deleting the first
        dummy = ListNode(0)
        dummy.next = head
        
        # traversing variable indicating where we are currently
        curr = dummy

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            # print(curr)
            else:
                curr = curr.next
        
        # we return the head 
        return dummy.next


        