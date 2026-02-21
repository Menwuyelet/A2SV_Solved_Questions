class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter_s = Counter(s)

        sorted_s = []
        # print(counter_s)
        # print(counter_s['b'])
        for chr in order:
            if chr in counter_s:
                temp = chr * counter_s[chr]
                sorted_s.append(temp)
                # print(sorted_s)
                counter_s[chr] = 0
        
        # print(sorted_s)

        for chr in counter_s:
            sorted_s.append(chr*counter_s[chr])
        
        return "".join(sorted_s)