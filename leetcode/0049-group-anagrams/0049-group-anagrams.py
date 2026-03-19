"""
- The question: given a list of strings we are tasked to return list of anagram words grouped to gether.(anagram words means they have the same elements but may differ in order)
- Solution:
    - so what we can do to solve this problem is check the chrs of each words and group these who has the same chrs.
    - to do that we can use dictionary and store each word as value with key being its sorted chrs.
    - this way words that are anagram will be grouped together.
    - at the end of the loop we just return the dictionary values casted to list.
-  Time and Space complexity:
    - Time = O(n*k log k), n = len(strs), k = len(words in strs)
    - space = O(n*k)
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            sortedS = sorted(s)
            ans["".join(sortedS)].append(s)
        return list(ans.values())

    
