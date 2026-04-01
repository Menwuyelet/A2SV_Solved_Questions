# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []

        inOrder(root, result)
        return result


def inOrder(node, result):
    if node:
        inOrder(node.left, result)

        result.append(node.val)

        inOrder(node.right, result)          