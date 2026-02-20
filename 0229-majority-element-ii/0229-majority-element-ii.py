"""
- The question: given the list of integers we are tasked to return the number that appears more than n//3 times
- Solution:
    - to do that we can use dictionary and iterate through each digit and count theire apperance.
    - after each appearance we check if the number meet the condition
    - if so we add it to our ans list else we continue.
    - after the loop ended we return the ans list.
-  Time and Space complexity:
    - Time = using sort: O(n), n = len(nums)
    - space = using sort: O(n), n = len(nume), this is because the ans list will only contain at most 2 elements.
"""

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