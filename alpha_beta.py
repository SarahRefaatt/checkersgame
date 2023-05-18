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


def choose_best_move(board, depth, maximizing_player):
    possible_moves = board.get_possible_moves(2 if maximizing_player else 1)
    best_move = None
    if maximizing_player:
        max_eval = float('-inf')
        for move in possible_moves:
            if board.is_valid_move(move):
                new_board = copy.deepcopy(board)
                new_board.apply_move(move, 2)
                eval, _ = alpha_beta(new_board, depth - 1, float('-inf'), float('inf'), False, None)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
    else:
        min_eval = float('inf')
        for move in possible_moves:
            if board.is_valid_move(move):
                new_board = copy.deepcopy(board)
                new_board.apply_move(move, 1)
                eval, _ = alpha_beta(new_board, depth - 1, float('-inf'), float('inf'), True, None)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
    return best_move