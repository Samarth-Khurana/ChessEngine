class GameState:
    def __init__(self):
        self.board = [
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"]
        ]
        self.whiteToMove = True
        self.moveLog = []

    def make_move(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.piece_moved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove


class movePieces:
    def __init__(self, board, sqstart, sqend):
        """

        :type board: object
        """
        self.startRow = sqstart[0]
        self.startCol = sqstart[1]
        self.endRow = sqend[0]
        self.endCol = sqend[1]
        self.piece_moved = board[sqstart[0]][sqstart[1]]
        self.piece_captured = board[sqend[0]][sqend[1]]

