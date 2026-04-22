# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder, postorder):
        post_map = {val: i for i, val in enumerate(postorder)}

        def build(preL, preR, postL, postR):
            if preL > preR:
                return None
            
            root = TreeNode(preorder[preL])
            
            if preL == preR:
                return root
            
            # next element in preorder is left child
            left_root_val = preorder[preL + 1]
            idx = post_map[left_root_val]
            
            left_size = idx - postL + 1
            
            root.left = build(preL + 1, preL + left_size, postL, idx)
            root.right = build(preL + left_size + 1, preR, idx + 1, postR - 1)
            
            return root
        
        return build(0, len(preorder) - 1, 0, len(postorder) - 1)