# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = 0
        slow = 0

        fast_curr = head
        slow_curr = head

        while fast_curr:
            fast += 1
            if fast % 2 == 0:
                slow += 1
                slow_curr = slow_curr.next
            fast_curr = fast_curr.next
        
        # if fast % 2 == 0:
        #     return slow_curr.next

        return slow_curr