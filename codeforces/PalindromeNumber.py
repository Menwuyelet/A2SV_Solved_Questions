"""
- The question: check if an intiger is palindrome or not.
- Solution:
    - to say a string(intiger) is palindrome it should be the same when read from front and read from back.
    - to check that we can use two colliding pointers to check if each counter chr on opposite of the half are the same.
    - if they are the same the string is palindrome else not.
    - to do that on intiger we should first convert it to string after that we can use the technique.
- Time and Space complexity:
    - Time = O(n/2) = O(n)
    - space = O(1)
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        left, right = 0, len(strX) - 1

        while left < right:
            if strX[left] != strX[right]:
                return False
            left += 1
            right -= 1
        return True
