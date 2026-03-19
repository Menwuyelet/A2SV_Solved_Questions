"""
- The question: we are given roman number and tasked to convert it to integer representation
- Solution:
    - we can solve thsi problem with easy iteration.
    - to do that we first map the base roman numbers to theire prespective integer.
    - after that we replace every compound number in the given roman number with its base numbers.
    - after that we just iterate throu the representation and increment our answer with the translation of the current roman number.
-  Time and Space complexity:
    - Time = O(2n + 2n + 2n + n) = O(n), n = len(s)
    - space = O(n), due to the replace method
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
                    "I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000
                }
        number = 0

        # replace comlex representations with thire primitive ones
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        for char in s:
            number += translations[char]
        return(number)