class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = {}      # key: player, value: their losses

        for winner,loser in matches:
            if winner not in losses:
                losses[winner] = 0
            losses[loser] = losses.get(loser, 0) + 1

        no_lost,one_lost = [],[]
        for player,loss_count in losses.items():
            if loss_count == 0:
                no_lost.append(player)
            elif loss_count == 1:
                one_lost.append(player)
        
        return[sorted(no_lost),sorted(one_lost)]