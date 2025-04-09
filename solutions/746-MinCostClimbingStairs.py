class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)

        for i in range(2,n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        
        return dp[-1]

"""
1. Create dp array that stores the minimum cost at every step
2. Have a for loop going from 2 to n+1
3. The last element in the dp array will be our answer
"""