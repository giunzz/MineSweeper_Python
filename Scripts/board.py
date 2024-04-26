import random
from Scripts.piece import Piece
# from game import Game
class Board:
    # def_vitural = 0
    def __init__(self, size, prob): # tạo bảng rỗng ban đầu
        self.size = size
        self.board = []
        self.won = False 
        self.lost = False
        self.prob = prob
        for row in range(size[0]):
            row = []
            for col in range(size[1]):
                bomb = 0  
                piece = Piece(bomb)
                row.append(piece)
            self.board.append(row)
    def update_board(self, board, index): # update bảng sau khi người chơi click
        cnt = 0
        sz = len(self.board)
        for i in range(sz):
            for j in range(sz):
                if (i == index[0] and j == index[1]): # bỏ qua vị trí user click lần đầu
                    continue
                else :
                    if cnt <= 1: 
                        bomb = 1 # bảng luôn có ít nhất 1 bom
                        cnt += 1
                    else: bomb = random.random() < self.prob #xác xuất 50% so với các bảng
                    piece = Piece(bomb)
                    self.board[i][j] = piece
            self.setNeighbors()
            self.setNumAround()

    def getBoard(self):
        return self.board

    def getSize(self):
        return self.size
    
    def getPiece(self, index):
        # print(self.board[index[0]][index[1]]) # dính bom là true get index khi user click
        return self.board[index[0]][index[1]]

    def handleClick(self, piece, flag):
        if piece.getClicked() or (piece.getFlagged() and not flag):
            return
        if flag:
            piece.toggleFlag()
            return
        piece.handleClick()
        if piece.getNumAround() == 0: # tiến hành loang rộng nếu ô click không có bom
            for neighbor in piece.getNeighbors(): # xung quanh có bom 
                self.handleClick(neighbor, False)
        if piece.getHasBomb():# gặp bom -> thua
            self.lost = True
        else:
            self.won = self.checkWon()
    
    def checkWon(self):
        for row in self.board:
            for piece in row:
                if not piece.getHasBomb() and not piece.getClicked(): # nếu  có bom và chưa click thì chưa thắng
                    return False
        return True

    def getWon(self):
        return self.won

    def getLost(self):
        return self.lost

    def setNeighbors(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                piece = self.board[row][col]
                neighbors = []
                self.addToNeighborsList(neighbors, row, col)
                piece.setNeighbors(neighbors)
    
    def addToNeighborsList(self, neighbors, row, col):
        for r in range(row - 1, row + 2): # xung quanh ô click 8 ô
            for c in range(col - 1, col + 2):
                if r == row and c == col: # trừ vị trí hiện tại
                    continue
                if r < 0 or r >= self.size[0] or c < 0 or c >= self.size[1]: # kích thước size[0] hàng , size[1] cột
                    continue
                neighbors.append(self.board[r][c]) # thêm vào list hàng xóm
    
    def setNumAround(self):
        for row in self.board:
            for piece in row:
                piece.setNumAround() #xét từng phần tử
        
        