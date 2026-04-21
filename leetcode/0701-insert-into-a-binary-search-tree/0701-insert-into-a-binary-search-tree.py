# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- The question: we are given a root of a binary search tree and a value and tasked to insert that value in the bst with out disrupting the bst.
- Solution:
    - this is basicaly a search problem.
    - that is we just search for the place that value should be and insert it there.
    - the thing that makes it easier is that we just go until we hit dead end and we create a new node and link it to that place.
-  Time and Space complexity:
    - Time = O(n log n), n = len(nodes)
    - space = O(n log n), 
"""

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        return insertion(root, val)
        

def insertion(node, val):
    # our base case
    if not node:
        return TreeNode(val)

    # if the value is at the left of our node we continue at the left
    if node.val > val:

        # we assign the newly created node to the left side of the ending node
        node.left = insertion(node.left, val)
        return node

    # if the value is at the right of our node we continue at the right
    elif node.val < val:

        # we assign the newly created node to the right side of the ending node
        node.right = insertion(node.right, val)
        return node
