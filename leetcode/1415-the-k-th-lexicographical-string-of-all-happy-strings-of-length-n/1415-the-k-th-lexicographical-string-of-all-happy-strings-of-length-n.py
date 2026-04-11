class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        maping = {}
        i = 1
        chrs = ['a', 'b', 'c']

        def backtrack(curr):
            nonlocal i
            if len(curr) == n:
                # print(maping)
                maping[i] = curr[:]
                i += 1
                return
            
            for chr in chrs:
                if (curr and chr != curr[-1]) or not curr:
                    curr.append(chr)

                    backtrack(curr)
                    curr.pop()
            
        backtrack([])
        return "".join(maping[k]) if k in maping else ""