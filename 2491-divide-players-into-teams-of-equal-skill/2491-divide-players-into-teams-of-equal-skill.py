class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        team_skill = sum(skill) / ( 0.5*len(skill) )
        
        skill.sort()
        
        chemistry = 0
        cnt = 0
        left = 0
        right = len(skill) - 1
        
        while right > left:
            sum_ = skill[left] + skill[right]
            
            if sum_ == team_skill:
                cnt += 1
                chemistry += skill[left] * skill[right]
                right -= 1
                left += 1
            elif sum_ < team_skill:
                left += 1
            else:
                right -= 1
                
        # return chemistry
                
        if cnt * 2 == len(skill):
            return chemistry
        else:
            return -1
        