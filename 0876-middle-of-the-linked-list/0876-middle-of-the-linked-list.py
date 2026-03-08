"""
- The question: we are given a linked list and tasked to return the midle node.
- Solution:
    - to achive this we can iterate through all the nodes and construct the index node mapping dictionary.
    - we can do better using two pointers just like on array
    - we will have two pointers, one fast and one slow ptr.
    - we move the fast ptr twice before we we move the slow ptr and by the time the fast ptr reachs the end, the slow reachs the midle
    - so we can return the node on the slow ptr.

-  Time and Space complexity:
    - Time = O(n), n = len of the linked list
    - space = O(1), 
"""
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
            
            # we update our slow_cur only after our fast have updated twice.
            if fast % 2 == 0:
                slow += 1
                slow_curr = slow_curr.next
            
            fast_curr = fast_curr.next

        return slow_curr