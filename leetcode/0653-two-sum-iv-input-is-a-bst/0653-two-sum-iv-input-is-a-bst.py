# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- The question: we are given a bst input and tasked to return True if there exist two elements that sum up to the target or False 
- Solution:
    - this problem is basicaly the two sum but with the input being bst
    - so the solution will be to generate an array using the inorder traversal of a tree and using that array to do the default two sum.
    - that it.
-  Time and Space complexity:
    - Time = O(n), n = num of nodes
    - space = O(h), h = recurssion stack
"""

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        ans = []

        # we construct the array using inorder traversal
        traverse(root, ans)

        # we perform the two sum on the constructed array
        return twoSum(ans, k)



def twoSum(ans, target):
    left = 0
    right = len(ans) - 1

    while left < right:
        if ans[left] + ans[right] == target:
            return True
        elif ans[left] + ans[right] > target:
            right -= 1
        else:
            left += 1
    return False

# we use recursive function to build the array to perform the two sum on
def traverse(node, ans):
    if not node:
        return 
    
    # we first iterate to the left side
    traverse(node.left, ans)
    
    # we append the last node to the array
    ans.append(node.val)

    # we then iterate to the right side of the tree
    traverse(node.right, ans)

    return 


