class Solution:
    def maxDepth(self, s: str) -> int:
        curDepth = 0
        res = 0
        for c in s:
            if c == "(":
                curDepth += 1
            elif c == ")":
                res = max(curDepth,res)
                curDepth -= 1
        return res