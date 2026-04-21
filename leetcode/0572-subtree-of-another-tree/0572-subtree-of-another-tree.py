# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- The question: we are a tree and another tree and tasked to determine if the second tree is a sub tree of the first one or not.
- Solution:
    - this seems hard but it is really easy to solve.
    - we just need to check if there is a subtree starting at each node with exact values as the given sub tree
    - if we find one we got our answer and return True, else False
    - to do that we use a function that iterates through both trees at the same time and check if they are the same.
    - we call this functions every time updating the current node and check for it
    - thats it.
-  Time and Space complexity:
    - Time = O(n * m), n = len(root), m = len(subtree)
    - space = O(h1 * h2), h1 = height of tree, h2 = height of subtree
"""

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # we check if the root is empty
        if not root:
            return False

        # we check if the current sub tree is the same as our given subtree by runing the helper function
        if check(root, subRoot):
            return True
        
        # we call it recursivly by changing the root to its left and right chileds
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


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