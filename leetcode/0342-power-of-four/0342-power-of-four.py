class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return check(n)

def check(n):
    if n == 1:
        return True
    elif n < 1:
        return False

    return check(n/4)