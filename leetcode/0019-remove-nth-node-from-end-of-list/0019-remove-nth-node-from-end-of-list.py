"""
- The question: we are given a linked list and we are tasked to delete the node nth form the end.
- Solution:
    - this is a linked list traversal problem, the trick is we delete the node nth from the end not from front.
    - so we must first knwow the index(order) of the nodes and after that we delete the node.
    - to track theire order we can use a dictinary with 1 based index as key and nodes as value. 
    - this way we can know the order of the nodes and access them with O(1)
    - after that we go to the node just before the node we want to delete and assigns its next to the node we want to delete next.
    - if the node we want to delete is head we just return head.next 
-  Time and Space complexity:
    - Time = O(n), n = len of the linked list due to the construction of the dictinary to track the order
    - space = O(n), 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        ref = {}
        idx = 1

        # we first construct a dictinary to store the nodes with index to access them in O(1)
        while curr:
            ref[idx] = curr
            curr = curr.next
            idx += 1

        length = idx - 1

        # removing the head
        if n == length:
            return head.next

        # we go to the node just before the node we want to delete and assign its next to the node we want to delete next
        prev = ref[length - n]
        prev.next = prev.next.next

        return head