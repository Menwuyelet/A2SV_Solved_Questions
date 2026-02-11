"""
- The question: we are given a string of chrs and tasked to sort these chrs based on ther frequency and return them as string
- Solution:
    - so this is basic sorting problem. we can use counter to store frequency of the chrs in string.
    - after that we sort the counter in reverse and iterate through it and append the chr to our ans.
-  Time and Space complexity:
    - Time = O(n + k*log k)​, n = len(s), k = number of unique chrachters in s which is at most 52, 
            - so O(n + 52*log 52) = O(n)
    - space = O(n) due to the list ans.
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)

        # sort the counter by its value in decreasing order
        sorted_counter = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
        
        ans = []
        # iterates over thr reverse sorted counter and append the chr to the ans 
        for chr in sorted_counter:
            temp = chr*sorted_counter[chr]
            ans.append(temp)
        
        return "".join(ans)
