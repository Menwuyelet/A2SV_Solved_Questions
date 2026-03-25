# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        
        nums = deque()
        
        temp = head

        while temp:
            nums.appendleft(temp.val)
            temp = temp.next
        
        for num in nums:
            if stack and stack[-1] > num:
                continue
            
            stack.append(num)

        stack = stack
        if stack:
            ans = ListNode(stack[-1])
            stack.pop()
            temp = ans

            while stack:
                nod = ListNode(stack[-1])
                temp.next = nod
                temp = temp.next
                stack.pop()
            
            return ans
        return 