"""
- The question: we are given a list of words and tasked to return the k most frequent ones, and if the frequency is the same order based on alphabetical order
- Solution:
    - we could solve this by counting and iterating over to biuld the answer.
    - but we could also used biultin nsmallest or nlargest methods form heapq module.
    - we first count the frequencies and use nsmallest method to return the k largest numbers with custom sorting key that sorts the first in deccending order and if same with assending order of the alphabet
    - to be able to use the method we should pair each word with its freq in a tuple and we use that to sort.
-  Time and Space complexity:
    - Time = O(n), n = len(words)
    - space = O(n), 
"""

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        # construct the freq count with pairing them 
        freq = Counter(words)
        words.clear()
        for word in freq:
            words.append((freq[word], word))
        
        # return the nsmallest tupls
        ans = nsmallest(k, words, key=lambda x: (-x[0], x[1]))

        # we unpack the tuple to return only the word
        for i in range(len(ans)):
            ans[i] = ans[i][1]
        
        return ans