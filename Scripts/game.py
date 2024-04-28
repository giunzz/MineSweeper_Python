import pygame, sys
from Scripts.board import Board 
from Scripts.bnt import Button
import os
from Scripts.solver import Solver
from Scripts import States
from time import sleep
import  sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font(resource_path("images/font.ttf"), size)


class Game:
    
    def __init__(self, size, prob):
        self.board = Board(size, prob)
        pygame.init()
        self.sizeScreen = 800, 800
        self.screen = pygame.display.set_mode(self.sizeScreen)
        self.pieceSize = (self.sizeScreen[0] / size[1], self.sizeScreen[1] / size[0]) 
        self.loadPictures()
        self.solver = Solver(self.board)
        

    def loadPictures(self):
        self.images = {}
        imagesDirectory = resource_path("images")
        for fileName in os.listdir(imagesDirectory):
            if not fileName.endswith(".png"):
                continue
            path = imagesDirectory + r"/" + fileName 
            img = pygame.image.load(path)
            img = img.convert()
            img = pygame.transform.scale(img, (int(self.pieceSize[0]), int(self.pieceSize[1])))
            self.images[fileName.split(".")[0]] = img
    
    def run(self):
        # print(self.prob)
        running = True
        k = 0
        while running:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and not (self.board.getWon() or self.board.getLost()):
                    rightClick = pygame.mouse.get_pressed(num_buttons=3)[2]
                    self.handleClick(pygame.mouse.get_pos(), rightClick,k)
                    if (k == 0): k = 1
                
                if event.type == pygame.KEYDOWN:
                    self.solver.move()
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()
            if self.board.getWon():
                sleep(2)
                self.win()
                running = False
            if self.board.getLost():
                sleep(2)
                self.lose()
                running = False
        pygame.quit()
        
    def draw(self):
        topLeft = (0, 0)
        for row in self.board.getBoard():
            for piece in row:
                rect = pygame.Rect(topLeft, self.pieceSize)
                image = self.images[self.getImageString(piece)]
                self.screen.blit(image, topLeft) 
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = (0, topLeft[1] + self.pieceSize[1])

    def getImageString(self, piece):
        if piece.getClicked():
            return str(piece.getNumAround()) if not piece.getHasBomb() else 'bomb-at-clicked-block'
        if (self.board.getLost()):
            if (piece.getHasBomb()):
                return 'unclicked-bomb'
            return 'wrong-flag' if piece.getFlagged() else 'empty-block'
        return 'flag' if piece.getFlagged() else 'empty-block'

    def handleClick(self, position, flag, k):
        index = tuple(int(pos // size) for pos, size in zip(position, self.pieceSize))[::-1] 
        if (k == 0) : self.board.update_board(self.board, index)
        else: self.board.handleClick(self.board.getPiece(index), flag)
    
    
    def win(self):
        SCREEN = pygame.display.set_mode((950, 700))
        BG = pygame.image.load(resource_path("images/Background.png"))
        pygame.display.set_caption("WIN")
        sound = pygame.mixer.Sound('music/win.wav')
        sound.play()   
        while True:
            SCREEN.blit(BG, (3, 5))

            MENU_MOUSE_POS = pygame.mouse.get_pos()
            
            MENU_TEXT = get_font(50).render("WIN", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(460, 100))

            HOME_BUTTON = Button(image=pygame.image.load(resource_path("images/Play Rect.png")), pos=(460, 250), 
                                text_input="HOME", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load(resource_path("images/Play Rect.png")), pos=(460, 400), 
                                text_input="QUIT", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
            SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [HOME_BUTTON,QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(SCREEN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if HOME_BUTTON.checkForInput(MENU_MOUSE_POS):
                        States.main_menu()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    def lose(self):
        SCREEN = pygame.display.set_mode((950, 700))
        BG = pygame.image.load(resource_path("images/Background.png"))
        pygame.display.set_caption("LOSE")
        sound = pygame.mixer.Sound('music/win.wav')
        sound.play()  

        # Load hình ảnh từ tệp tin
        image1= pygame.image.load(resource_path("images/a1.png"))

        # Lấy kích thước của hình ảnh
        image_rect1 = image1.get_rect()

        



        while True:
            SCREEN.blit(BG, (3, 5))
            SCREEN.blit(image1, (300, 500))

            MENU_MOUSE_POS = pygame.mouse.get_pos()
            
            MENU_TEXT = get_font(50).render("LOSE", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(460, 100))

            HOME_BUTTON = Button(image=pygame.image.load(resource_path("images/Play Rect.png")), pos=(460, 250), 
                                text_input="HOME", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load(resource_path("images/Play Rect.png")), pos=(460, 400), 
                                text_input="QUIT", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
            SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [HOME_BUTTON,QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(SCREEN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if HOME_BUTTON.checkForInput(MENU_MOUSE_POS):
                        States.main_menu()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
    
