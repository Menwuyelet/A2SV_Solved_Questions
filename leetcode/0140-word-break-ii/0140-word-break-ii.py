"""
- The question: we are given a string s and word dict containing some words and tasked to return all the possible sentences created by using the chrs in the s forming words inside the word dict.
- Solution:
    - so the solution is a brute force approach that uses backtracking to explore every posible choices.
    - we iterate over the string s one chr at a time and we check if that word is in the worddict adn if so we add it to our descision tree and go to the next one.
    - after reaching th end we backtrack to the explore other choices.
    - we do that for every possible clasfication and that it is.
-  Time and Space complexity:
    - Time = O(2^2), n = len(s), m = posible valid words constructed for chr from s
    - space = O(m), 
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        # we make the word dict set for better lookup
        wordDict = set(wordDict)

        def backtrack(i):

            # if our i reached the last index we append the current words joined by space to make them one sentence
            if i == len(s):
                res.append(" ".join(temp))
                return
            
            # we iterate starting from the current index to the last to explore every choice 
            for j in range(i, len(s)):
                word = s[i:j+1]

                # if it is avalid word we append it to our temp list and do a backtrack to explore next choices
                if word in wordDict:
                    temp.append(word)
                    backtrack(j+1)

                    # after reaching the final choice we backtrack to explore other options
                    temp.pop()
                
        res = []
        temp = []

        # we start our backtracking with the first index
        backtrack(0)
        
        return res