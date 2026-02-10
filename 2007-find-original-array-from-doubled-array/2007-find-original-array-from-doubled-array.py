class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2 == 1:
            return []

        counter = Counter(changed)
        changed.sort()
        ans = []

        for num in changed:
            if num == 0 and (counter[num] > 1):
                counter[num] -= 2
                ans.append(num)
            elif num != 0 and (counter[num] and counter[num*2]):
                counter[num] -= 1
                counter[num*2] -= 1
                ans.append(num)
        
        # print(ans)
        if len(ans) == len(changed)//2:
            return ans
        return []