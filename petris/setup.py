import pygame

from config import WINDOWWIDTH, WINDOWHEIGHT

pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
FONT_PATH = pygame.font.match_font('dejavusans')
BASICFONT = pygame.font.Font(FONT_PATH, 18)
BIGFONT = pygame.font.Font(FONT_PATH, 100)
pygame.display.set_caption('Petrisy')
