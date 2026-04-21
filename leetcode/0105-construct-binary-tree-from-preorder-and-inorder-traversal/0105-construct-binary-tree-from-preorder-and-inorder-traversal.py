# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
- The question: we are given a preorder and inorder traversal of a tree and tasked to construct the tree.
- Solution:
    - we can do that by recursivley solve for the left and right subtree of each nodes.
    - to do that we take the property that the first element of preorder traversal is always the root of the tree.
    - and the elements before the root node in the in order traversal is always the elements of the left side sub tree elements, after are the elements of the right side subtree.
    - we use these properties recursively to construct the tree.
-  Time and Space complexity:
    - Time = O(n^2), n = len(nodes)
    - space = O(n^2), 
"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # allways the first elements in the preorder traversal is the root
        root = TreeNode(preorder[0])

        # we take the mid indx to figure out the left and right side of the tree
        mid = inorder.index(preorder[0])
        
        # we biuld the left and right side of the trees recursively.
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

