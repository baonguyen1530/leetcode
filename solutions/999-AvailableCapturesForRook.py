class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for r in range(8):
            for c in range(8):
                if board[r][c] == "R":
                    rook_row = r
                    rook_col = c
                    break
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        result = 0

        for dr,dc in directions:
            nr,nc = rook_row,rook_col
            while 0 <= nr < 8 and 0 <= nc < 8:
                nr += dr
                nc += dc
                if not(0 <= nr < 8 and 0 <= nc < 8):
                    break
                if board[nr][nc] == "B":
                    break
                if board[nr][nc] == "p":
                    result += 1
                    break
                
        return result