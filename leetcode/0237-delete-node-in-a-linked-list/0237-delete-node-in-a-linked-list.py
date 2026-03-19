"""
- The question: we are given a node of a linked list and we are tasked to remove it. but he head of the linked list wont be given.
- Solution:
    - so the solution would be to take the node next to the given node and copy it to the given node and after that set the next of the given node to the next of the next node.
    ex. [4, 2, 3, 1], if we are given 2 as our node to delete, we take 3 and copy it to the value of 2. and we set the next of 2 to 1.
-  Time and Space complexity:
    - Time = O(1), 
    - space = O(1), 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # set the value of the given node to the value of the next node.
        node.val = node.next.val

        # set the next of the given node to the next of the next node
        node.next = node.next.next
    