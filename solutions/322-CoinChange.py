""" 
My first inital thought is to use a decision tree, but that would have extra computation which will increase time complexity
Hint: DP-bottom up, which means start from 0 and go up
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        # 1-12
        for a in range(1, amount + 1):
            # [1,2,5]
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1