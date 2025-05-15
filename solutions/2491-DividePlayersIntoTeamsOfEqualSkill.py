class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total_skill = sum(skill)
        n = len(skill)
        team = n / 2
        
        if total_skill % team != 0:
            return -1

        skill_required = total_skill / team
        skill.sort()
        left = 0
        right = n - 1
        result = 0

        while left < right:
            if skill[right] + skill[left] != skill_required:
                return -1
            result += skill[right] * skill[left]
            left += 1
            right -= 1
            
        return result