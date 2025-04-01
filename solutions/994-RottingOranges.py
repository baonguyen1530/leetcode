class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW,COL = len(grid),len(grid[0])
        fresh_oranges,minute = 0,0
        
        #adding the rotten oranges into the queue
        queue = deque()

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        # while queue is not empty
        # and fresh_oranges is greater than 0
        # we will keep running the loop

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while queue and fresh_oranges > 0:
            for i in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in directions:
                    row,col = r+dr,c+dc
                    if (row < 0 or row == ROW or col < 0 or col == COL or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    fresh_oranges -= 1
                    queue.append((row,col))
            minute += 1

        return minute if fresh_oranges == 0 else -1