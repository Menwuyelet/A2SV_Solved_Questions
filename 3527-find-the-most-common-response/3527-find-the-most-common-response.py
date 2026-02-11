class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = defaultdict(int)
        common = ["", 0]
        for response in responses:
            seen = set()
            for ans in response:
                if ans not in seen:
                    seen.add(ans)
                    count[ans] += 1
                    if common[1] < count[ans]:
                        common[0] = ans
                        common[1] = count[ans]
                    elif common[1] == count[ans]:
                        common[0] = min(common[0], ans)
            
        return common[0]