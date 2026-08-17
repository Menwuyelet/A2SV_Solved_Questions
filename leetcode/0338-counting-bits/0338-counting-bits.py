class Solution:
 def countBits(self, n: int) -> List[int]:
    count = []

    for i in range(n+1):
        curr = 0

        while i > 0:
            if i & 1 == 1:
                curr += 1

            i >>= 1

        count.append(curr)

    return count