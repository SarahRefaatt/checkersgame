from board import Board
from minimax import get_all_moves
from copy import deepcopy
import pygame
import copy
import minimax


def alpha_beta(position, depth, alpha, beta, maximizing_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), None

    if maximizing_player:
        value = float('-inf')
        best_move = None
        for move in get_all_moves(position, maximizing_player, game):
            new_board = copy.deepcopy(position)

            ab, _ = alpha_beta(new_board, depth - 1, alpha, beta, False, game)
            value = max(value, ab)
            alpha = max(alpha, value)
            if alpha >= beta:
                best_move = move
                break
            best_move = move
        return value, best_move
    else:
        value = float('inf')
        best_move = None
        for move in get_all_moves(position, maximizing_player, game):
            new_board = copy.deepcopy(position)

            ab, _ = alpha_beta(new_board, depth - 1, alpha, beta, True, game)
            value = min(value, ab)
            beta = min(beta, value)
            if alpha >= beta:
                best_move = move
                break
            best_move = move
        return value, best_move
