class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return (False)
        S_count = Counter(s)
        T_count = Counter(t)
        return (S_count == T_count)
       