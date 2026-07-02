from functools import lru_cache

class Solution:
    def beautifulArray(self, n: int):
        @lru_cache(None)
        def build(n):
            if n == 1:
                return [1]

            odds = build((n + 1) // 2)
            evens = build(n // 2)

            return [2 * x - 1 for x in odds] + [2 * x for x in evens]

        return build(n)