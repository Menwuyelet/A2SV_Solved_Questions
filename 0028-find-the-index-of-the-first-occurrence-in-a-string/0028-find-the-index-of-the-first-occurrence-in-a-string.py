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
                h_ptr = ans + 1
                n_ptr = 0
                ans = 0
            else:
                h_ptr += 1
        
        return -1