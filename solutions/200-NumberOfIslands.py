class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        island = 0

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            
            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                #check if the surrounding grid is valid or not
                for dr, dc in directions:
                    r,c = row + dr, col + dc
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == "1" and (r,c) not in visited:
                        #add it to the queue
                        q.append((r,c))
                        #add the row and col to the visisted set
                        visited.add((r,c))
                    

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    island += 1
        
        return island

"""
Check if the grid is empty, if it is empty then return 0 because there will be no island
Initialize two global variables ROWS and COLS
    ROWS is the length of the grid
    COLS is the length of the each array in grid
Also initialize a set to keep track of all of the visited grid and the total of island
We will go through every grids and check if that grid is '1', if it is then we will run bfs to find how big the island will be
For our bfs function, check every direction and continute checking until it reaches the max column/row or we encounter water
"""