class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter
        chars_count = Counter(chars)
        ans = 0
        for word in words:
            word_count = Counter(word)
            l = 0
            for chrs in word:
                if word_count[chrs] > chars_count.get(chrs, 0):
                    l = 0
                    break
                l = len(word)
            ans+=l 
            
        return ans


        #         count_a = Counter(a)
        # count_b = Counter(b)

        # for x in count_b:
        #     if count_b[x] > count_a.get(x, 0):
        #         return False
        # return True