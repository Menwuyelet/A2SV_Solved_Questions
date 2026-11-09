# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []

        postOrder(root, result)

        return result

def postOrder(node, result):
    if node:
        
        postOrder(node.left, result)
        
        postOrder(node.right, result)

        result.append(node.val)