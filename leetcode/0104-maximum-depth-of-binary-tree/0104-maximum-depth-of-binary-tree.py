# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- The question: we are given a root of a binary tree and tasked to return the max depth
- Solution:
    - this is really just dfs traversing problem.
    - we traverse the tree with dfs and count the depth and return the max.
    - to do that we use recursive approach with not node as base case and returning 0
    - and left, right recursive callse and return 1 + max(left, right) recursive relation
-  Time and Space complexity:
    - Time = O(n), n = len(nodes), d = max depth
    - space = O(d), 
"""


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        ans = traverse(root)
        return ans
    
def traverse(node):

    # when we reach the leaf node and calls the traverse it gets 0 as return 
    if not node:
        return 0
    
    # we traverse left first 
    left = traverse(node.left)

    # then right
    right = traverse(node.right)
    
    # return the max depth between left and right
    return 1 + max(left, right)
