"""
- The question: given a string and number of oprations we are tasked to create the longest substring with a repeating charachters.
                - to create that we can choose any charachter to any other charachter as long as we dont do it more times than the given k.
- Solution:
    - we just need to count the number of characters in a the window we have and try to change the chrachters with the smallest count to the charachter with the more count.
    - then check if the current window is maximum or not. 
    - we iterate until we reach the end of the string s.
-  Time and Space complexity:
    - Time => O(n), n = max(len(num1), max(num(2)))
    - space = O(n)
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        ans = 0
        left = 0
        maxcount = 0

        for right in range(len(s)):
            count[s[right]] += 1
            maxcount = max(maxcount, count[s[right]])

            while (right - left + 1) - maxcount > k:
                count[s[left]]-= 1
                left += 1
                
            ans = max(ans, right - left + 1)

        return ans