# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        
        def sub_tree(node):
            nonlocal max_sum
            if not node:
                return 0
            
            left_gain = max(sub_tree(node.left), 0)
            right_gain = max(sub_tree(node.right), 0)
            
            current_path_sum = node.val + left_gain + right_gain
            
            max_sum = max(max_sum, current_path_sum)
            
            return node.val + max(left_gain, right_gain)
        
        sub_tree(root)
        return max_sum       