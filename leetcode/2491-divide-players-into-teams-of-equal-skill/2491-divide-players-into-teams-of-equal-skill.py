class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        left_ptr, right_ptr = 0, len(skill) - 1

        team_skill = skill[0] + skill[-1]

        ans = 0
        while left_ptr < right_ptr:
            if team_skill != skill[left_ptr] + skill[right_ptr]:
                return -1
            
            ans += (skill[left_ptr] * skill[right_ptr])
            left_ptr += 1
            right_ptr -= 1

        return ans

