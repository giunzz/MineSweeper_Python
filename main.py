import sys
from Scripts.game import Game
import pygame
import os

def play():
    size = (12,12) #int(sys.argv[1]), int(sys.argv[2])
    prob = 0.1 #float(sys.argv[3])
    pygame.display.set_caption('Minesweeper')
    clock = pygame.time.Clock()
    g = Game(size, prob)
    g.run()

if __name__ == '__main__':
    play()