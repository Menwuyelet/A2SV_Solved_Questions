"""
- The question: given a list of numbers we are thasked to return the k most repeated numbers.
- Solution:
    - to solve this problem we use counter to count the frequency of the numbers and sort them in reverse.
    - after that we iterate through the sorted list up to k and print the first k elements.
-  Time and Space complexity:
    - Time = O(n), n = len(num)
    - space = O(n)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_count = dict(sorted(count.items(), key=lambda item : item[1], reverse=True))
        ans = []
        for i, key in enumerate(sorted_count):
            if i >= k:
                break
            ans.append(key)
        return ans