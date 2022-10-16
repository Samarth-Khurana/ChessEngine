from typing import Tuple

import pygame as p
from Chess import ChessEngine

p.init()
WIDTH = HEIGHT = 512
DIMENSIONS = 8
SQ_SIZE = HEIGHT // DIMENSIONS
MAX_FPS = 15
IMAGES = {}


def load_images():
    pieces = ['wp', 'wQ', 'wK', 'wR', 'wB', 'wN', 'bp', 'bQ', 'bK', 'bR', 'bB', 'bN']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = ChessEngine.GameState()

    load_images()
    running = True
    sq_selected: tuple = ()
    move = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sq_selected == (row, col):
                    sq_selected = ()
                    move = []

                else:
                    sq_selected = (row, col)
                    if len(move) == 0:
                        if gs.board[row][col] != "--":
                            move.append(sq_selected)
                    else:
                        move.append(sq_selected)
                if len(move) == 2:
                    mv = ChessEngine.movePieces(gs.board, move[0], move[1])
                    gs.make_move(mv)
                    sq_selected = ()
                    move = []

        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


def draw_game_state(screen, gs):
    draw_chess_board(screen)
    draw_pieces(screen, gs.board)


def draw_chess_board(screen):
    colours = [p.Color("white"), p.Color("purple")]
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            col = colours[(r + c) % 2]
            p.draw.rect(screen, col, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_pieces(screen, board):
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
