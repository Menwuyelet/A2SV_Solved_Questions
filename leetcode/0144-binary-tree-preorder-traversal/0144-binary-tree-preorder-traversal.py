# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def preorder(result, node):
    if node:
        result.append(node.val)
        
        preorder(result, node.left)
        preorder(result, node.right)
    
    return
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        preorder(result, root)
        return result
    