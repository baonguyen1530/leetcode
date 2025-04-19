class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        # going 
        for i in range(len(s)-1,-1,-1):
            # going through every word in wordDict
            for w in wordDict:
                # check if the current word window is less than the actual word (if the current word window is longer than it's impossible to find a segment)
                # if the current word window is the same as the word in wordDict then we have found a segment
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                # this is here to remove any unnecessary work
                # if the dp[i] is already true then we don't have to check the other words in wordDict
                if dp[i]:
                    break
        
        return dp[0]