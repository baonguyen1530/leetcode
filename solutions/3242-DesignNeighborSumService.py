class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid

    def diagonalSum(self, value: int) -> int:
        self.ROW,self.COL = len(self.grid),len(self.grid[0])
        for row in range(self.ROW):
            for col in range(self.COL):
                if self.grid[row][col] == value:
                    self.total = 0
                    directions = [(-1,-1),(-1,1),(1,-1),(1,1)]
                    for dr,dc in directions:
                        new_row,new_col = row+dr,col+dc
                        if 0 <= new_row < self.ROW and 0 <= new_col < self.COL:
                            self.total += self.grid[new_row][new_col]
                    return self.total

    def adjacentSum(self, value: int) -> int:
        self.ROW,self.COL = len(self.grid),len(self.grid[0])
        for row in range(self.ROW):
            for col in range(self.COL):
                if self.grid[row][col] == value:
                    self.total = 0 
                    directions = [(-1,0),(1,0),(0,1),(0,-1)]
                    for dr,dc in directions:
                        new_row,new_col = row+dr,col+dc
                        if 0 <= new_row < self.ROW and 0 <= new_col < self.COL:
                            self.total += self.grid[new_row][new_col]
                    return self.total


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)