class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # first we will find every region that won't be able to be surrounded in in the board
            # these regions aren't surrounded because they will be on the edge
        ROW,COL = len(board),len(board[0])
        no_connect = set()

        def dfs(r,c,visit):
            if (r < 0 or c < 0 or r == ROW, c == COL or board[r][c] != "O"):
                return
            visit.add((r,c))
            dfs(r+1,c,visit)
            dfs(r-1,c,visit)
            dfs(r,c+1,visit)
            dfs(r,c-1,visit)

        # 1.Capture the unsurronded regions
        for r in range(ROW):
            for c in range(COL):
                if (board[r][c] == "O") and (r in [0,ROW-1] or c in [0,COL-1]):
                    dfs(r,c,no_connect)
        
        for r in range(ROW):
            for c in range(COL):
                if (board[r][c] == "O" and (r,c) not in no_connect):
                    board[r][c] = "X"