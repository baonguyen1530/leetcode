class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        result = (rungs[0] - 1) // dist

        for i in range(len(rungs)-1):
            result += (rungs[i+1] - rungs[i] - 1) // dist

        return result