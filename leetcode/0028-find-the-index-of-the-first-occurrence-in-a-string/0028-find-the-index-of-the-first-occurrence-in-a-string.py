"""
- The question: we are given two strings and tasked to find if the second string exsists in the first and if so return the starting index, else return -1

- Solution:
    - we can solve this problem easily using find() python biult in function.
    - but we will use two pointers to solve it in brute force since the constraints allows it.
    - we use tow pointers one in each string and we iterate until we hit the end of the first string or find our answer.
    - when we iterate we check if the current chr in first string is equal to the chr in the second strings first posision.
    - if so we initiate the matching loop. we go through the element comparing the current element of the first sting to the current element of the second string.
    - if we hit the end of the second string it means we found our match and return the starting posision.
    - but if we break, we hit missmatch so we start from the begining seting the ptr of the first string to the index 1+ to the index we initiated the matching loop, the ptr of the second to 0 to start over.
-  Time and Space complexity:
    - Time = O(n * m), n = len(haystack), m = len(needle)
    - space = O(1)
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_ptr = 0
        n_ptr = 0

        ans = 0

        while h_ptr < len(haystack):
            if haystack[h_ptr] == needle[n_ptr]:
                ans = h_ptr
                while h_ptr < len(haystack) and n_ptr < len(needle) and haystack[h_ptr] == needle[n_ptr]:
                    h_ptr += 1
                    n_ptr += 1
                
                if n_ptr == len(needle):
                    return ans
                
                # we set our ptrs to thiere state before to begin the search again
                h_ptr = ans + 1
                n_ptr = 0
                ans = 0

            else:
                h_ptr += 1
        
        return -1