# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
- The question: we are given a root of a tree and tasked to return the sum of all the nodes that have a grand parent with even value.
- Solution:
    - to do this we just use basic bfs using qeue and track currnt node, its parent, and grandparent 
    - and every time we pop from our qeue we check its grandparent and if it meets the condition we add it to our sum. else we just continue
-  Time and Space complexity:
    - Time = O(n), n = len(nodes)
    - space = O(n), 
"""

class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        nodes = deque([(root, None, None)])
        ans = 0

        # we iterate over our qeue and check for every node
        while nodes:
            # we unpack the poped value of the deque
            curr, parent, grandparent = nodes.pop()

            # if our current node have a grand parent with even value we add it to our sum
            if grandparent and grandparent.val % 2 == 0:
                ans += curr.val

            # we add the left and right nodes of our current node to the qeue
            if curr.left:
                nodes.append((curr.left, curr, parent))
            
            if curr.right:
                nodes.append((curr.right, curr, parent))
        
    
        return ans