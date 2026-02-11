class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        sorted_counter = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
        
        print(sorted_counter)
        ans = ""
        for chr in sorted_counter:
            temp = chr*sorted_counter[chr]
            ans = "".join([ans, temp])
        return ans