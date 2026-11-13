# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
- The question: we are given a root of a binary search tree and a value and tasked to delete that value in the bst with out disrupting the bst.
- Solution:
    - this is a search and ordering problem.
    - that is we just search for the place that value is and delete it with out disrupting the bst.
    - the thing we should consider 3 cases,
            - first the value is a leaf node, in that case we just delete it and move on
            - second the value have only one chiled node, in that case we delete the node and replace it with its chiled.
            - third the value have two chiled nodes, in that case we find the inorder succssor of the value and replace it with that and delete it.
-  Time and Space complexity:
    - Time = O(n), n = len(nodes)
    - space = O(n), 
"""

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return deleteNode(root, key)
      

def deleteNode(root, key):
    # Return if the tree is empty
    if not root:
        return root

    # Find the node to be deleted
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif(key > root.val):
        root.right = deleteNode(root.right, key)
    else:
    # If the node is with only one child or no child
        if not root.left and not root.right:
            return None
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left

    # If the node has two children,
    # place the inorder successor in position of the node to be deleted
        temp = minValueNode(root.right)
        root.val = temp.val
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.val)
    return root

# Find the inorder successor
def minValueNode(node):
    current = node
    # Find the leftmost leaf
    while current.left:
        current = current.left
    return current