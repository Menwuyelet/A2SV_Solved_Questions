# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_list = ListNode(0)
        odd_list = ListNode(0)

        curr_even = even_list
        curr_odd = odd_list

        curr = head
        idx = 1
        while curr:
            # if our current index is even we add the current node at the even list
            if idx % 2 == 0:
                curr_even.next = curr
                curr_even = curr_even.next
            
            # if our current index is odd we add the current node at the odd list
            else:
                curr_odd.next = curr
                curr_odd = curr_odd.next
            idx += 1
            curr = curr.next
        
        # we set the last of the even_list to none to avoid pointing to the old values of the last node pointing to   
        curr_even.next = None
        curr_odd.next = even_list.next

        return odd_list.next