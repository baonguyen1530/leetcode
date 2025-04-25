class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offside = 1
        
        for i in range(1,n+1):
            if offside*2 == i:
                offside = i
            dp[i] = 1 + dp[i - offside]
        
        return dp