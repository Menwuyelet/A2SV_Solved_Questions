"""
- The question: given two words we are tasked to check if the two words are close or not. to say two words are close we must be able to obtain one from the others.
                - we can perform two oprations to make them close
                    1, swap two existing chrs in one word
                    2, exchange the identity of two chrs.
- Solution:
    - the question asks if we can make them close not to make them close.
    - so what we really need to check is if it is posible to use these oprations and make them close.
    - so we can check two conditions that make it imposible and if these conditions are not meet we can make the two words close.
    - the two conditions are:
            1, if the two words dont conatian the same words
            2, if the frequency pattern of the of the two words dont match.
    - if these two conditions are false we can make them clse else we cant.
-  Time and Space complexity:
    - Time = O(n long n), n = len(word1)
    - space = O(1), because we only get 26 unique letters. 
"""
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # this checks that the two words contain the same characters
        if set(word1) != set(word2):
            return False
        
        # this checks if the two words have same frequency pattern or not 
        if sorted(Counter(word1).values()) != sorted(Counter(word2).values()):
            return False
        
        return True
