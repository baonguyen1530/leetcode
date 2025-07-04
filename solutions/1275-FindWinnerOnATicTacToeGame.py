class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3 
        rows, cols = [0] * n, [0] * n
        diag1 = diag2 = 0

        for index, move in enumerate(moves):
            # i is the row
            # j is the column
            i, j = move
            sign = 1 if index % 2 == 0 else -1
            rows[i] += sign
            cols[j] += sign
            if i == j:
                diag1 += sign
            if i + j == n - 1:
                diag2 += sign
            print(f"{rows} {cols} {diag1} {diag2}")
            if abs(rows[i]) == n or abs(cols[j]) == n or abs(diag1) == n or abs(diag2) == n:
                return "A" if sign == 1 else "B"
        return "Draw" if len(moves) == (n * n) else "Pending"