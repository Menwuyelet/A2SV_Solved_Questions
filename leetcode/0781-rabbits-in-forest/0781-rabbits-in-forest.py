class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        seen = Counter(answers)

        ans = 0

        for rabit, grp in seen.items():
            group = rabit + 1
            tot = (grp + rabit) // group
            ans += tot * group
            
        return ans

            # count = Counter(answers)
            # ans = 0

            # for k, v in count.items():
            #     group_size = k + 1
            #     groups = (v + k) // group_size   # ceil(v / group_size)
            #     ans += groups * group_size

            # return ans