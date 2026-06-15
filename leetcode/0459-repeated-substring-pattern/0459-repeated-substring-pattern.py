class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for i in range(1, n // 2 + 1):
            # substring length must divide total length
            if n % i == 0:
                pattern = s[:i]

                # repeat pattern enough times
                if pattern * (n // i) == s:
                    return True

        return False