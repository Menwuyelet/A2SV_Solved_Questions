class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        lis = range(1, n+1)
        res = []

        targetPtr = 0
        lisPtr = 0

        while targetPtr < len(target) and lisPtr < n:
            ans.append("Push")
            res.append(lis[lisPtr])
            if target[targetPtr] == lis[lisPtr]:
                targetPtr += 1
                lisPtr += 1
            else:
                ans.append("Pop")
                res.pop()
                lisPtr += 1

            if res == target:
                return ans
            