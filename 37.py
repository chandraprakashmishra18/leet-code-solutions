class Solution:
    def solveSudoku(self, board):
        def valid(r, c, ch):
            for i in range(9):
                if board[r][i] == ch:
                    return False
                if board[i][c] == ch:
                    return False

                br = 3 * (r // 3) + i // 3
                bc = 3 * (c // 3) + i % 3

                if board[br][bc] == ch:
                    return False
            return True

        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for ch in "123456789":
                            if valid(r, c, ch):
                                board[r][c] = ch
                                if solve():
                                    return True
                                board[r][c] = "."
                        return False
            return True

        solve()