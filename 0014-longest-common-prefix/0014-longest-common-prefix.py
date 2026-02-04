"""
- The question: we are asked to find the longes common prefix given an array of words.
- Solution:
    - so to solve this we can use two for loops to iterate throug the list and check for the first missmatch or the first word to run out of chrs.
    - when we do that we iterate using two loops, the first loop will iterate from 0 to the length of the first word on the list. 
    - and the inner loop will run throug all the words on the list lenght of the first word times. 
    - inside this loop we will check if the current chr on the first word is the same as the current chr on the current word.
    - additionaly we check if the current index is greater than or equal to the current word length.
    - if any of the above conditions meet we return the ans list we created by joinig it.
    - else we append the current chr to the ans list after every compleet iteration of the inner loop. 
-  Time and Space complexity:
    - Time = O(n*k), k = to the length of the first word due to the two loops
    - space = O(n), due to the creation of the ans list.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        for i in range(len(strs[0])):
            for word in strs:
                if i >= len(word) or strs[0][i] != word[i]:
                    return ("").join(ans) 
            ans.append(word[i])
        return ("").join(ans) 