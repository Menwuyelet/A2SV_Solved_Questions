class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            sortedS = sorted(s)
            ans["".join(sortedS)].append(s)
        return list(ans.values())

    