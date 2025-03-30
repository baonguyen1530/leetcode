class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # same thing as (200) number of island problem but we will keep track of the number of island as well
        if not grid:
            return 0

        largest_island = 0
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()

        def bfs(r,c):
            num_islands = 1
            queue = collections.deque()
            queue.append((r,c))
            visited.add((r,c))
            
            while queue:
                r,c = queue.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    row,col = r+dr,c+dc
                    if row in range(ROW) and col in range(COL) and grid[row][col] == 1 and (row,col) not in visited:
                        visited.add((row,col))
                        queue.append((row,col))
                        num_islands += 1
                        
            return num_islands

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r,c) not in visited:
                    # bfs function will return the number of island
                    # and then we will compare it to the largest_island
                    largest_island = max(largest_island, bfs(r,c))
        
        return largest_island