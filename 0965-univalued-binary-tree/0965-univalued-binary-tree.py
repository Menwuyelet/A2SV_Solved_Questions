# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        que = deque()

        que.append(root)

        while que:
            node = que.popleft()
            if node.val != root.val:
                return False

            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

        
        return True