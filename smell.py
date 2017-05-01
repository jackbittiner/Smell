import pygame, sys
from pygame.locals import *

FPS = 200

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

def main():
    pygame.init()
    global DISPLAY_SURF
    FPSCLOCK = pygame.time.Clock()
    DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Smell')
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
