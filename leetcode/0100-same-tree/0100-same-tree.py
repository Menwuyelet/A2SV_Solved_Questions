# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- The question: we are given two trees and tasked to determine if they are the same tree
- Solution:
    - we can iterate over the two trees at the same time and we could check the values wethere they are the same or not
    - to do that we iterate using depth first iterativly both trees at the same time.
    - we also consider three cases, both empty, only one empty, and both not empty.

-  Time and Space complexity:
    - Time = O(n), n = nums of nodes
    - space = O(h), h = height of the tree
"""

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        return check(p, q)



def check(p, q):

    # we return True if both the trees are empty
    if not p and not q: 
        return True

    # we return False if only one of the trees are empty
    if not p or not q:
        return False

    # if both are not empty and the values are not equal, we return False
    if p.val != q.val:
        return False

    # all the aboves are base cases we check them recursivly
    return check(p.left, q.left) and check(p.right, q.right)

    