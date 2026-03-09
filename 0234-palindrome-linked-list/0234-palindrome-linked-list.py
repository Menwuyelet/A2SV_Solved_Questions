"""
- The question: we are given a linked list and tasked to determine wether the given number is palindrom or not
- Solution:
    - so to solve this problem we can use two pointers technique and solve it efficiently.
    - one thing is we cant really use coliding ptrs on a linked list.
    - so we construct an array from the given linked list and after that we use coliding pointers to check for palindrome.
-  Time and Space complexity:
    - Time = O(n), n = length of the given linked list
    - space = O(n), 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array = []

        curr = head
        # iterate through the linked list and construct an array to perform the two ptr approach
        while curr:
            array.append(curr.val)
            curr = curr.next

        left, right = 0, len(array)-1
        # we iterate throught the constructed array using left and right ptr and check if it is palindrome or not
        while left < right:
            if array[left] != array[right]:
                return False
            
            left += 1
            right -= 1

        return True
