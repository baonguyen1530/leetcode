class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * (n+1)
        dp[0],dp[1] = 1,1
        
        for i in range(2, n + 1):
            # for one digit
            one_digit = int(s[i - 1])
            # for two digits
            two_digit = int(s[i - 2:i])

            if 1 <= one_digit <= 9:
                dp[i] += dp[i-1]
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        
        return dp[-1]