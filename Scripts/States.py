import sys
from Scripts.game import Game
import pygame
from Scripts.bnt import Button


pygame.init()

SCREEN = pygame.display.set_mode((950, 700))
pygame.display.set_caption("Menu")

BG = pygame.image.load("images/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("images/font.ttf", size)



def play(n):
    size = (n,n) 
    if (n == 4):
        prob = 0.1
    elif (n == 10):
        prob = 0.2
    else:
        prob = 0.3
    pygame.display.set_caption('Minesweeper')
    g = Game(size, prob)
    g.run()

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def guide():
    
    # SCREEN = pygame.display.set_mode((1950, 700))
    
    while True:
        SCREEN.blit(BG, (3, 5))
        MAIN_TEXT = get_font(50).render("MINESWEEPER", True, "#b68f40")
        MAIN_RECT = MAIN_TEXT.get_rect(center=(500, 100))
        SCREEN.blit(MAIN_TEXT,MAIN_RECT)
        text = "Minesweeper is also known by another name called Mine Detection or Bomb Removal. Coming to Minesweeper"\
        "the player's task is to open all the squares without clicking on the squares containing mines, and if you click on a square containing a mine, you will lose immediately"\
        ". You can right-click to place a flag."
        
        font = pygame.font.SysFont('Arial', 25)

        GUIDE_MOUSE_POS = pygame.mouse.get_pos()
        
        TEXT_BUTTON = Button(image=pygame.image.load("images/Quit Rect.png"), pos=(500, 280),text_input="0", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
        
        RETURN_BUTTON = Button(image=pygame.image.load("images/Options Rect.png"), pos=(400, 400), 
                                text_input="RETURN", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("images/Quit Rect.png"), pos=(400, 550), 
                                text_input="QUIT", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        
        
        for button in [RETURN_BUTTON, QUIT_BUTTON, TEXT_BUTTON]:
            button.changeColor(GUIDE_MOUSE_POS)
            button.update(SCREEN)
            blit_text(SCREEN, text, (100, 200), font, pygame.Color('white'))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if RETURN_BUTTON.checkForInput(GUIDE_MOUSE_POS):
                        main_menu()
                    if QUIT_BUTTON.checkForInput(GUIDE_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (3, 5))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("MINESWEEPER", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("images/Play Rect.png"), pos=(460, 250), 
                            text_input="START", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        GUIDE_BUTTON = Button(image=pygame.image.load("images/Options Rect.png"), pos=(460, 400), 
                            text_input="GUIDE", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("images/Quit Rect.png"), pos=(400, 550), 
                            text_input="QUIT", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, GUIDE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Options()
                if GUIDE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    guide()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def Options():
    while True:
        SCREEN.blit(BG, (3, 5))

        OPTION_MOUSE_POS = pygame.mouse.get_pos()

        OPTION_TEXT = get_font(50).render("OPTIONS", True, "#b68f40")
        OPTION_RECT = OPTION_TEXT.get_rect(center=(500, 100))

        OP1 = Button(image=pygame.image.load("images/Play Rect.png"), pos=(460, 250), 
                            text_input="EASY", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        OP2 = Button(image=pygame.image.load("images/Options Rect.png"), pos=(460, 400), 
                            text_input="MEDIUM", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        OP3 = Button(image=pygame.image.load("images/Quit Rect.png"), pos=(400, 550), 
                            text_input="HARD", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(OPTION_TEXT, OPTION_RECT)
        for button in[OP1,OP2,OP3]:
            button.changeColor(OPTION_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OP1.checkForInput(OPTION_MOUSE_POS):
                    play(4)
                if OP2.checkForInput(OPTION_MOUSE_POS):
                    play(9)
                if OP3.checkForInput(OPTION_MOUSE_POS):
                    play(19)

        pygame.display.update()
        
# if __name__ == '__main__':
#     main_menu()