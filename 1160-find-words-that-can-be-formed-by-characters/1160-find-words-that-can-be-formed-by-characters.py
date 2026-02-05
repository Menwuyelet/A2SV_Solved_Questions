"""
- The question: given list of words and a string, we are tasked to find the total sum of length of the words from the given list that are formed from the chars that are present in the given string.
              - the number of apperance of a charachter in word must not exceed the number of apperance in the chars string.
- Solution:
    - we can store the chars from the chars string and iterate through the words list and compare the count of charachters inside a word againist 
    - the chars count and if one of the chars in word have greater count that the chars count we add nothing else we add len(word) to ans
    - at the end of the outer iteration we return ans.
-  Time and Space complexity:
    - Time = using sort: O(c+n*m) = O(100+100⋅n) ≈ O(100⋅n), n = len(words), m = len(word), c = len(chars)
    - space = using sort: O(c), using set: O(1)
"""

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter
        chars_count = Counter(chars)
        ans = 0
        for word in words:
            word_count = Counter(word)
            word_len = len(word)

            for chrs in word:
                if word_count[chrs] > chars_count.get(chrs, 0):
                    word_len = 0
                    break
        
            ans+=word_len
            
        return ans
