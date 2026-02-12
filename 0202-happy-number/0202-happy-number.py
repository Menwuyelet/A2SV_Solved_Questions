class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum_of_squared_digits(n)
        return True
        # print(sum_of_squared_digits(19))
    
def sum_of_squared_digits(n):
    digits = str(n)
    sum_ = 0
    for digit in digits:
        # print(digit)
        sum_ += pow(int(digit), 2)

    return sum_