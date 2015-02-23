import pygame, sys
from pygame.locals import *

pygame.init()

windowsSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello world')

BACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

basicFont = pygame.font.SysFont(None, 48)
