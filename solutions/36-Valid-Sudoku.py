class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        C = collections.defaultdict(set)
        R = collections.defaultdict(set)
        S = collections.defaultdict(set)  # key = (r/3, c/3)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if(board[row][col] in R[row]
                or board[row][col] in C[col]
                or board[row][col] in S[row//3,col//3]):
                    return False
                R[row].add(board[row][col])
                C[col].add(board[row][col])
                S[row//3, col//3].add(board[row][col])
        return True