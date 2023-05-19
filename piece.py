from constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN
import pygame


class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
            raduis = SQUARE_SIZE // 2 - (self.PADDING)
            pygame.draw.circle(win, GREY, (self.x, self.y), raduis + self.OUTLINE)
            pygame.draw.circle(win, self.color, (self.x, self.y), raduis)
            if self.king:
                # to make the image in the centre
                win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    def _repr_(self):
            return str(self.color)

    def move(self, row, col):
            self.row = row  # new row
            self.col = col  # new col
            self.calc_pos()  # tell the position of x , y godad

