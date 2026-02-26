class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        leftPtr, rightPtr = 0, len(skill)-1
        ans = 0
        teamSkill = skill[leftPtr] + skill[rightPtr]
        while leftPtr < rightPtr:
            if skill[leftPtr] + skill[rightPtr] != teamSkill:
                return -1
            ans += skill[leftPtr] * skill[rightPtr]
            leftPtr += 1
            rightPtr -= 1
        return ans

