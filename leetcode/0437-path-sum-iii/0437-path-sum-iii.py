# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = {0: 1}

        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            
            # number of valid paths ending here
            count = prefix.get(curr_sum - targetSum, 0)
            
            # add current sum to prefix map
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
            
            # explore children
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            
            # backtrack
            prefix[curr_sum] -= 1
            
            return count
        
        return dfs(root, 0)