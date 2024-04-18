import sys
from Scripts.game import Game
import pygame
from Scripts.bnt import Button
import os


pygame.init()

SCREEN = pygame.display.set_mode((950, 700))
pygame.display.set_caption("Menu")

BG = pygame.image.load("images/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("images/font.ttf", size)



def play():
    size = (21,21) #int(sys.argv[1]), int(sys.argv[2])
    prob = 0.2 #float(sys.argv[3])
    pygame.display.set_caption('Minesweeper')
    # clock = pygame.time.Clock()
    # print(clock.get_fps())
    g = Game(size, prob)
    g.run()


def main_menu():
    while True:
        SCREEN.blit(BG, (3, 5))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("MINESWEEPER", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("images/Play Rect.png"), pos=(460, 250), 
                            text_input="PLAY", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("images/Options Rect.png"), pos=(460, 400), 
                            text_input="OPTIONS", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("images/Quit Rect.png"), pos=(460, 550), 
                            text_input="QUIT", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        
if __name__ == '__main__':
    main_menu()