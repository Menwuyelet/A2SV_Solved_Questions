# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
- The question: we are given a linked list containing integers and tasked to remove all the nodes that have a node to theire right with higher value.
- Solution:
    - we can solve this problem by constructin a stack that contains all the valid nodes and return a new linked list with all the valid nodes.
    - to do that we first convert our linked list to list.
    - after that we iterate over it in reverse order and extract only the valid nodes and store thire value.
    - we extract the valid nodes by using a monotonically increasing stack. 
    - that is to append the current node there must not be any node greater than it befor it(since we reversed it).
    - after we construct our stack we iterate over it and bilud our linked list and return it.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(n),
"""
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        
        nums = deque()
        
        # we iterate over the given linked list to make it a list in reverse order.
        temp = head
        while temp:
            nums.appendleft(temp.val)
            temp = temp.next
        
        # we iterate over our constructed list and extract the valid nodes using monotonically increasing stack 
        # with slight modification to not include non valid nodes
        for num in nums:

            # we just keep moving if the current node have a node greater than it before it
            if stack and stack[-1] > num:
                continue
            
            stack.append(num)

        # we iterate over our mono-increasing stack and biuld our linked list, we check if there are any valid nodes first
        if stack:
            ans = ListNode(stack[-1])
            stack.pop()

            temp = ans

            # we iterate over our stack and take its top element and add it to our linked list and pop it from our stack
            while stack:
                nod = ListNode(stack[-1])
                temp.next = nod
                temp = temp.next

                stack.pop()
            
            # return our linked list
            return ans

        # if there are no valide nodes we return empty list(nothing)
        return 