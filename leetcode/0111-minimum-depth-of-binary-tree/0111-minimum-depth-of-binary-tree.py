# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
- The question: we are given a root of a binary tree and tasked to return the min depth
- Solution:
    - this is really just dfs traversing problem.
    - we traverse the tree with dfs and count the depth and return the min.
    - to do that we use recursive approach with not node as base case and returning 0
    - and left, right recursive callse and return 1 + min(left, right) recursive relation
    - the one case is that the path should reach leaf node so if no atleast one node after the parent for root node it takes the other path even though the other is minimum
-  Time and Space complexity:
    - Time = O(n), n = len(nodes), d = max depth
    - space = O(d), 
"""


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        ans = traverse(root)
        return ans


def traverse(node):
    if not node:
        return 0

    # if not left path we take the right
    if not node.left:
        return 1 + traverse(node.right)
    # if not right path we take the left 
    if not node.right:
        return 1 + traverse(node.left)

    # else both exisist we take min of the two
    left = traverse(node.left)
    right = traverse(node.right)

    return 1 + min(left, right)