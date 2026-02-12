"""
- The question: we are given a string of digits and tasked to find A valid pair defined as two adjacent digits in s such that:
    . The first digit is not equal to the second.
    . Each digit in the pair appears in s exactly as many times as its

- Solution:
    - since we are tasked to find tow adjecent pairs that are not equal, we iterate up to len(s) - 1 and compare s[i], s[i+1] and comfirm they are not equal.
    - after we find a pair that is valid we check their frequency in the s. to do that we first store their frequency in counter.
    - if they are appearing the same time as their value we return them.
    - if we didn't find such pair we return empty string.
-  Time and Space complexity:
    - Time = O(n), n = len(nums)
    - space = O(n), 
"""
class Solution:
    def findValidPair(self, s: str) -> str:
        counter = Counter(s)

        for i in range(len(s)-1):
            curr_chr = s[i]
            next_chr = s[i+1]
            curr_num = int(s[i])
            next_num = int(s[i+1])

            # checks if the current chr and the next chr are not equal, and checks the frequency of both current and next chrs to insure they appear as their value
            if curr_chr != next_chr and counter[curr_chr] == curr_num and counter[next_chr] == next_num:
                return f"{s[i]}{s[i+1]}"
       
        return ""