import pygame, sys
from pygame.locals import *

FPS = 200

WINDOWWIDTH = 400
WINDOWHEIGHT = 300

LINETHICKNESS = 10
PADDLESIZE = 50
PADDLEOFFSET = 20

BLACK = (0,186,0)
WHITE = (255,69,255)
global DISPLAYSURF
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

def main():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Smell')
    ballX = WINDOWWIDTH/2 - LINETHICKNESS/2
    ballY = WINDOWHEIGHT/2 - LINETHICKNESS/2

    playerOnePosition = (WINDOWHEIGHT - PADDLESIZE)/2
    playerTwoPosition = (WINDOWHEIGHT - PADDLESIZE)/2

    paddle1 = pygame.Rect(PADDLEOFFSET, playerOnePosition, LINETHICKNESS, PADDLESIZE)
    paddle2 = pygame.Rect(WINDOWWIDTH-PADDLEOFFSET-LINETHICKNESS, playerTwoPosition, LINETHICKNESS, PADDLESIZE)

    ball = pygame.Rect(ballX, ballY, LINETHICKNESS, LINETHICKNESS)

    drawArena()
    drawPaddle(paddle1)
    drawPaddle(paddle2)
    # drawBall(ball)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def drawArena():
    DISPLAYSURF.fill((0,0,0))
    pygame.draw.rect(DISPLAYSURF, WHITE, ((0,0),(WINDOWWIDTH,WINDOWHEIGHT)), LINETHICKNESS*2)
    pygame.draw.line(DISPLAYSURF, WHITE, ((WINDOWWIDTH/2),0),((WINDOWWIDTH/2),WINDOWHEIGHT), (LINETHICKNESS/4))

def drawPaddle(paddle):
    if paddle.bottom > WINDOWHEIGHT - LINETHICKNESS:
        paddle.bottom = WINDOWHEIGHT - LINETHICKNESS
    elif paddle.top < LINETHICKNESS:
        paddle.top = LINETHICKNESS
    pygame.draw.rect(DISPLAYSURF, WHITE, paddle)


if __name__ == '__main__':
    main()

# drawArena()
