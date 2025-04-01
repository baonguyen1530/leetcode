class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW,COL = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addRoom(r,c): 
            if (r < 0 or r == ROW or c < 0 or c == COL or (r,c) in visit or grid[r][c] == -1):
                return
            visit.add((r,c))
            q.append((r,c))

        # find the position of all the treasure chests
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        distance = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = distance
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            distance += 1

'''
First we want to find the position of the every treasure on the grid, then from there we traverse outward using BFS while keeping track of the distance and modify the grid.
'''