# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = defaultdict(int)

        dummy = ListNode(0)
        dummy.next = head

        curr = dummy

        while curr and curr.next:
            # if the count of the next node is 1 we remove the next node form our list since it is duplicated
            if count[curr.next.val] == 1:
                curr.next = curr.next.next
            # else we add it to our counter for future refrences
            else:
                count[curr.next.val] += 1
                curr = curr.next
    
        return dummy.next