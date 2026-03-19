"""
- The question: given a pattern and string s we are tasked after key value paring pattern and each words from the s, to determine wether the s follows the pattern. 
              - each letter in pattern can only paired with one unique word, and every word is allowed to paire with unique letter.
- Solution:
    - so to solve this we can use hash map and set.
    - first we check if the length of pattern is equal to length of the list of the words, since one is les there is duplicate which is not allowed.
    - if they are not equal we return false and we are done.
    - else: we use seen_word set to store already mapped words to check for uniqueness, s_pattern_map to map the pattern and word.
    - we iterate through the pattern and check if the letter is already patterned.
    - if so we check if it is paired with diffrent word thatn the current we return false and break.
    -else we check if the current word is already paired from our seen_word and if so we return false and break.
    - if it passed both the conditions we map the letter and the current word to our map and add the word to seen_word.
    - after we iterate through the pattern if the program is still runing means we dont have and unvalid map so we return true and break.
-  Time and Space complexity:
    - Time = O(n), n = len(list_s),
    - space = O(n * m), m = number of unique words
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_s = s.split(" ")

        # if length differ there must be duplicate so we return false
        if len(pattern) != len(list_s):
            return False
        
        seen_word = set()
        s_pattern_map = {}

        for idx, chr in enumerate(pattern):
            current_word = list_s[idx]
            # if the letter is already maped and not maped to the current word we return false 
            if chr in s_pattern_map.keys():
                if s_pattern_map[chr] != current_word:
                    return False
            # if the current word is mapped before it means it is maped to another letter so we return false
            elif current_word in seen_word:
                return False
            
            seen_word.add(current_word)
            s_pattern_map[chr] = current_word
            
        return True
