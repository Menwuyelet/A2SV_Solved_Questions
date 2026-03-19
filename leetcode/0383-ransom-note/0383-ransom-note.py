"""
- The question: given tow strings we are tasked to determine wether the first string can be constructed from the second one without using the same chr more than 1s.
- Solution:
    - this is basic counting problem.
    - we count both strings chrs and compare by iterating through the both strings to check wether the chr exists in the second string or not.
-  Time and Space complexity:
    - Time = O(n + m), n = len(ransomNote), len(magazine)
    - space = O(1)
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_ransomNote = Counter(ransomNote)
        counter_magazine = Counter(magazine)

        for key, value in counter_ransomNote.items():
            if key not in counter_magazine or counter_magazine[key] < value:
                return False
        
        return True