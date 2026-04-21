"""
- The question: we are given a list of chrs and tasked to reverse the list in place
- Solution:
    - this is very easy problem that we could solve using the biult in methods, but we are not supposted to do that.
    - so we will solve it by implimenting it.
    - we could solve this in difrent ways using two pointers and recursion
    - in both approachs we swap the tow oposit chrs that is how it will become reversed.
-  Time and Space complexity:
    - Time = O(n), n = len(heights)
    - space = O(n), 
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        # Two pointer way
        # two_ptr(s, left, right)
        
        # Recursive way
        swap(s, left, right)


# Using two pointers
def two_ptr(s, left, right):

    # we iterate until our left and right match or pass eachother and swap the two opposite chrs
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Recursive way
def swap(s, left, right):

    # if our left and right are equal or past eachother we hit our base case
    if left >= right:
        return
    
    # we call it recursivly by incrementing the left and decrementing the right
    swap(s, left + 1, right - 1)

    # this is our real acction takes place we swap the two opposit chrs
    s[left], s[right] = s[right], s[left]

    return 