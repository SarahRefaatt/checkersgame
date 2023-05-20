import pygame
from constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE
from piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def evaluate(self):
        return self.white_left - self.red_left + (self.white_kings * 0.5 - self.red_kings * 0.5)

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for i in range(ROWS):
            # interior list for each row
            self.board.append([])
            for j in range (COLS):
                # we can drop white or red
                # for example at row = 0, col = 0 , row = 1 not equal
                # row = 1 , col = 1 hisawo b3d fhn7ot cube
                if j%2 == (i+1)%2 :
                    if i < 3 :
                        self.board[i].append(Piece(i,j,WHITE))
                    elif i > 4 :
                        # m3na keda 2n da fare3 tany khlas f h7ot pieces bta3to
                        self.board[i].append(Piece(i,j,RED))
                    else :
                        # wala keda wala keda m3na keda 2ne da morb3 alhsebo fady baa
                        self.board[i].append(0)
                else:
                    ## da morb3 alhsebo fadyy 
                    self.board[i].append(0)

    def draw(self,win):
        # rhis function to draw a piece on the window
        self.draw_squares(win)
        for i in range(ROWS):
            for j in range(COLS):
                # fe piece de hib2a feha y zero  yrkm white y rkm red
                piece = self.board[i][j]
                if piece !=0:
                    #m3na keda 2n gwaha haga fhrsmha 3ala window
                    piece.draw(win)

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1

    def winner(self):
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return RED

        return None

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.king:
            #3shaan el red byb2aa mn fo2 le taht fa 3shaan kdaa row -1 ka start w row-3 ka end wel 3aks fel white
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
            
        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = [] #gwahaa el last piece
        for r in range(start, stop, step): row,row ,directiom
            if left < 0:##bafdal a3ml left - ama fel right +1
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:#lw fe list of skipped w fnfs el wa2t el last piece ana fehaa fadyaa
                    break
                elif skipped:#lw fee haga hyt3mlhaa skip sa3thaa ha3ml move w hatb2aa skip +last 3shaan awsl lel makan gded
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last#hafdal zay manaa

                if last:
                    if step == -1:#direction bel -ve sa3thaa ha3ml operation bel -
                        row = max(r - 3, 0)#3shaan bashtaghl 3ala 3 rows mn 3andy mn awl 0 le 3
                    else:
                        row = min(r + 3, ROWS)#mn awl 8 le taht be 3
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))#el skipped homaa hyb2oo el last le2ny haba2a already 3adethoom
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:##da ma3naa enyy maynf3sh athark 3lehaa aw lehhaa fa kdaa ha break w ashoof el ba3doo
                break
            else:
                last = [current]

            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:#akher el columns
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves
