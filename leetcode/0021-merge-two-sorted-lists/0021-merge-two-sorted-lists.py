# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        
        curr1 = list1
        curr2 = list2
        curr_dummy = dummy
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                temp = ListNode(curr1.val)
                curr_dummy.next = temp
                curr_dummy = curr_dummy.next
                curr1 = curr1.next
            else:
                temp = ListNode(curr2.val)
                curr_dummy.next = temp
                curr_dummy = curr_dummy.next
                curr2 = curr2.next

        if curr1:
            curr_dummy.next = curr1
        
        if curr2:
            curr_dummy.next = curr2
        
        return dummy.next