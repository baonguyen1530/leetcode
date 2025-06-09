class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        rows = [sorted(i) for i in nums]
        return sum(max(row[i] for row in rows) for i in range(len(rows[0])))