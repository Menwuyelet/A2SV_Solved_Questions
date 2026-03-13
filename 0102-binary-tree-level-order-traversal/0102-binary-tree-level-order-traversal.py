# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = deque()
        que.append(root)

        if not root:
            return []

        ans = []

        while que:

            temp = []
            length = len(que)
            for _ in range(length):
                node = que.popleft()
                temp.append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
            
            ans.append(temp)
                    

        return ans