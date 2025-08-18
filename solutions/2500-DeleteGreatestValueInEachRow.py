class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        result = []
        for i in range(len(grid[0])):
            temp = []
            for row in grid:
                max_num = max(row)
                temp.append(max_num)
                row.remove(max_num)
            result.append(max(temp))
        return sum(result)