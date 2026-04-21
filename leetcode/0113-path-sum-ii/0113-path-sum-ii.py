# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- The question: given a node of a tree and a target sum, we are tasked to list all the paths that start at the root and end at the leaf that give the target when summed.
- Solution:
    - this is the same question as the path sum 1 which is prety easy, we just traverse depth first and add the nodes and return True if there is a path that gives the target, else false.
    - we take that solution and we convert it to backtracking to list all the possible paths we check all the combinations backtracking.
    - that is it.
-  Time and Space complexity:
    - Time = O(n * h), n = num of nodes, h = height of the tree
    - space = O(n * h)
"""

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        # if the given tree is empty we return empty list
        if not root:
            return []

        tot = 0
        ans = []
        def traverse(node, tot, curr):
            
            # our base case 
            if not node:
                return
            
            # we add the value of the current node to our total and append it to our currnt list
            tot += node.val
            curr.append(node.val)

            # we check if out node is leaf node and the target is meet if so we append the current list to our answer and backtrack by poping the current node to go back
            if not node.left and not node.right and tot == targetSum:
                ans.append(curr[:])
                curr.pop()
                return

            # we travers to the left side of the tree and then to the right
            traverse(node.left, tot, curr)
            traverse(node.right, tot, curr)

            # if we found the leaf node but the target is not meet we just pop and backtrack 
            curr.pop()

        # we call our traverse with initial variables tot with 0 value and empty curr value 
        traverse(root, tot, [])

        return ans

