class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # how can you tell if the current cell reaches one of the ocean?
        # start from the ocean and going inside to the cell
        # we keep track of all the cell that can reach the oceans
        # and the cells that can reach both will be added to the result set
            # traversing wiose, we will use dfs??
        ROW,COL = len(heights),len(heights[0])
        pacific,atlantic = set(),set()  # this will store the cells that can reach either pacific or atlantic

        def dfs(r, c, visit, prevHeight):
            if(r < 0 or r == ROW or c < 0 or c == COL or heights[r][c] < prevHeight or (r,c) in visit):
                return
            visit.add((r,c))
            # visit its neighbor
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        for c in range(COL):
            # we traverse through the first row
            # these cells are all connected to the pacific ocean
            dfs(0, c, pacific, heights[0][c])
            dfs(ROW-1, c, atlantic, heights[ROW-1][c])

        for r in range(ROW):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COL-1, atlantic, heights[r][COL-1])

        result = []
        for r in range(ROW):
            for c in range(COL):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        
        return result