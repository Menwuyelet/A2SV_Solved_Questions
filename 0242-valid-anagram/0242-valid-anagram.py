"""
- The question: given two strings we are tasked to check wether string t is anagram of string s.
- Solution:
    - to say two words anagram of eachother they both should have same length and same chr and frequency.
    - to solve this problem we can use counter to count the frequncies of the chrs in each strings and check wether they are equal or not.
-  Time and Space complexity:
    - Time = O(n + n), O(n) n = len(s)
    - space = O(n),
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return (False)
        S_count = Counter(s)
        T_count = Counter(t)
        return (S_count == T_count)
       