class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        k = 2
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        so_count = dict(sorted(count.items(), key=lambda item : item[1], reverse=True))
        ans = []
        for i, key in enumerate(so_count):
            if i >= k:
                break
            ans.append(key)
        return ans