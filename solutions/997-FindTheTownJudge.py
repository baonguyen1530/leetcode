class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        Trusted = [0] * (n+1)
        for (a,b) in trust:
            Trusted[a] -= 1     #lose a trust
            Trusted[b] += 1     #gain a trust
        
        for i in range(1,len(Trusted)):
            #if this person has exactly n - 1 trust
            #that means they must be the judge?
            if Trusted[i] == n - 1:
                return i
        return -1
