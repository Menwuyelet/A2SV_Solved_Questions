# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr):
            if not curr:
                return [0, 0]
            
            left_size, left_coin = dfs(curr.left)
            right_size, right_coin = dfs(curr.right)

            size = 1 + left_size + right_size
            coins = curr.val + left_coin + right_coin
            self.res += abs(size - coins)
            return [size, coins]
        
        dfs(root)
        return self.res