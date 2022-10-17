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

    def allValidMoves(self):
        self.allPossibleMoves()

    def allPossibleMoves(self):
        moves = []
        for r in range(8):
            for c in range(8):
                x = self.board[r][c][0]
                if (x == 'w' and self.whiteToMove) or (x == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    if piece == 'p':
                        self.getPawnMoves(r, c, moves)
                    elif piece == 'R':
                        self.getRookMoves(r, c, moves)
                    elif piece == 'N':
                        self.getKnightMoves(r, c, moves)
                    elif piece == 'B':
                        self.getBishopMoves(r, c, moves)
                    elif piece == 'Q':
                        self.getQueenMoves(r, c, moves)
                    elif piece == 'K':
                        self.getKingMoves(r, c, moves)
        return moves

    def getPawnMoves(self, r, c, moves):
        if self.whiteToMove:
            if r == 1 and self.board[r + 2][c] == "--" and self.board[r + 1][c] == "--":
                moves.append(movePieces(self.board, (r, c), (r + 2, c)))

            if r < 7 and self.board[r + 1][c] == "--":
                moves.append(movePieces(self.board, (r, c), (r + 1, c)))
            if r < 7 and c >= 1 and self.board[r + 1][c - 1][0] == "b":
                moves.append(movePieces(self.board, (r, c), (r + 1, c - 1)))
            if r < 7 and c <= 6 and self.board[r + 1][c + 1][0] == "b":
                moves.append(movePieces(self.board, (r, c), (r + 1, c + 1)))
        else:
            if r == 6 and self.board[r - 2][c] == "--" and self.board[r - 1][c] == "--":
                moves.append(movePieces(self.board, (r, c), (r - 2, c)))
            if r > 0 and self.board[r - 1][c] == "--":
                moves.append(movePieces(self.board, (r, c), (r - 1, c)))
            if r > 0 and c >= 1 and self.board[r - 1][c - 1][0] == "w":
                moves.append(movePieces(self.board, (r, c), (r - 1, c - 1)))
            if r > 0 and c <= 6 and self.board[r - 1][c + 1][0] == "w":
                moves.append(movePieces(self.board, (r, c), (r - 1, c + 1)))

    def getRookMoves(self, r, c, moves):
        pass

    def getKnightMoves(self, r, c, moves):
        pass

    def getBishopMoves(self, r, c, moves):
        pass

    def getQueenMoves(self, r, c, moves):
        pass

    def getKingMoves(self, r, c, moves):
        pass


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
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol
        print(self.moveID)

    def __eq__(self, other):
        if isinstance(other, movePieces):
            return self.moveID == other.moveID
