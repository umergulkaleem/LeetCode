class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [["" for _ in range(3)] for _ in range(3)]

        for i, (row, col) in enumerate(moves):
            board[row][col] = 'X' if i % 2 == 0 else 'O'

        def is_winner(symbol):
            for i in range(3):
                if all(board[i][j] == symbol for j in range(3)) or \
                   all(board[j][i] == symbol for j in range(3)):
                    return True
            if all(board[i][i] == symbol for i in range(3)) or \
               all(board[i][2 - i] == symbol for i in range(3)):
                return True
            return False

        if is_winner('X'):
            return "A"
        elif is_winner('O'):
            return "B"
        elif len(moves) == 9:
            return "Draw"
        else:
            return "Pending"


            
        