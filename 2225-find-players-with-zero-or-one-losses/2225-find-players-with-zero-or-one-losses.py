class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = [[], []]
        team_won_lost = {}
        first_team, last_team = float('inf'), -float('inf')
        for match in matches:
            first_team = min(first_team, min(match))
            last_team = max(last_team, max(match))
            
            team_won_lost[match[0]] = team_won_lost.get(match[0], {})
            team_won_lost[match[0]]['won'] = team_won_lost[match[0]].get('won', 0)+1
            
            team_won_lost[match[1]] = team_won_lost.get(match[1], {})
            team_won_lost[match[1]]['lost'] = team_won_lost[match[1]].get('lost', 0)+1
        
        for team in range(first_team, last_team+1):
            if team not in team_won_lost:
                continue
            if team_won_lost[team].get('lost', 0)==0:
                answer[0].append(team)
            elif team_won_lost[team]['lost']==1:
                answer[1].append(team)
        return answer