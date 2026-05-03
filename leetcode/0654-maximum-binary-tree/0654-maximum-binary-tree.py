# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- The question: given a list of integers we are tasked to construct a binary tree that the max element will be a node for each left and right subtrees.
- Solution:
    - we solve this using a recursive approach.
    - we have a base case of when len(nums) == 1 and len(nums) = 0
    - when it is 1 we just create a node and return it else if it is 0 we return empty
    - if it is nither we findout the index of the local maximum, then create a node with it then we call left and right spliting the list on that indx and biuld the left and right iteratively.
    - after that we assight the left and right to our root node for each subt ree and retrun that root.
    
-  Time and Space complexity:
    - Time = O(n^2), n = len(nums)
    - space = O(n), 
"""
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def biuld(nums):

            # if len is 1 that means we only have one element so we do not need to split we just return it as node
            if len(nums) == 1:
                nod = TreeNode(nums[0])
                return nod

            # if it is 0, that means we dont have a node for that split so we return null
            if len(nums) == 0:
                return 

            # if it is more than 1 we findout the local maximum and its idx then create a node for it.
            idx = max_indx(nums)
            nod = TreeNode(nums[idx])

            # arter that we split the list on that idx and call biuld to the left and right to biuld the left and right sub trees
            left = biuld(nums[:idx])
            right = biuld(nums[idx+1:])

            # we assight the returned left and right subtrees to our node and return it
            nod.left = left
            nod.right = right

            return nod
        
        return biuld(nums)


# a func used to return the index of the maximum given a list
def max_indx(lis):
    num = max(lis)
    return lis.index(num)