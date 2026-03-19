"""
- The question: we are given a linked list and tasked to to partition it in tow parts. the first one contains elements of the nodes with odd indices and the second one contains the even indices node values. and we are tasked to do the partitioning in O(1) extra space
- Solution:
    - this problem is same with another leetcode problem the only diffrent is the partitioning criteria and the constraint of using O(1) space.
    - we could solve it with O(n) space with the same approach as the other problem but since this requires O(1) we change our approach.
    - we use three variables odd, even and even_head to trak our current node for both even and odd indices and to store the head of the even ones for later use.
    - we iterate through the linked list and we assign odd.next the even.next and we set the odd tracker to the new end of odd
    - after that we set the even.next to odd.next and again we set the even to current even end.
    - after we finish this we assign the odd.next to the head of the even to link the two lists and return the head.
    - this solve it with O(1) extra space.
-  Time and Space complexity:
    - Time = O(n), n = length of the given linked list
    - space = O(1), 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if the linked list is empty or only have one node we return simply the head
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        # we set the end of odd node point to the head of the start of the even nodes
        odd.next = even_head

        return head
