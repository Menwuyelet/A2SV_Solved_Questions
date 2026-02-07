class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        val = len(nums)//3
        visited = defaultdict(int)
        ans = set()
        for i in nums:
                visited[i] += 1
                if visited[i] > val:
                    ans.add(i)

        return(list(ans))