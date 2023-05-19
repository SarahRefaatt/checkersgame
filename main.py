import pygame
from constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from game import Game
from minimax import minimax
import random
from alpha_beta import alpha_beta


import time

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def get_row_col_random():
    row = random.randint(0, 7)
    col = random.randint(0, 7)
    return row, col


def main(choice,level):
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            if (choice==1):
                value,new_board=alpha_beta(game.get_board(), 4,float( '-inf'), float('inf'), WHITE,game)

            else:
                value, new_board = minimax(game.get_board(), 4, WHITE, game)

            game.ai_move(new_board)


        if game.winner() != None:
            print(game.winner())
            run = False



        if level==2 :
            value, new_board = minimax(game.get_board(), 4, RED, game)
            game.ai_move(new_board)

        elif level==3 :
           value, new_board = alpha_beta(game.get_board(), 4, float('-inf'), float('inf'), RED, game)
           game.ai_move(new_board)
        else:
            row, col = get_row_col_random()
            game.select(row, col)



        game.update()

    pygame.quit()
