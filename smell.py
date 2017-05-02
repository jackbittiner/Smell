import pygame, sys
from pygame.locals import *

FPS = 1000

WINDOWWIDTH = 800
WINDOWHEIGHT = 600

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

    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 20
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    player_1_score = 0
    player_2_score = 0

    paddle1 = pygame.Rect(PADDLEOFFSET, playerOnePosition, LINETHICKNESS, PADDLESIZE)
    paddle2 = pygame.Rect(WINDOWWIDTH-PADDLEOFFSET-LINETHICKNESS, playerTwoPosition, LINETHICKNESS, PADDLESIZE)
    ball = pygame.Rect(ballX, ballY, LINETHICKNESS, LINETHICKNESS)

    ballDirX = -1 ## -1 = left 1 = right
    ballDirY = -1 ## -1 = up 1 = down



    drawArena()
    drawPaddle(paddle1)
    drawPaddle(paddle2)
    drawBall(ball)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_q]: paddle1.move_ip(0,-10)
        if pressed[pygame.K_a]: paddle1.move_ip(0,10)
        if pressed[pygame.K_p]: paddle2.move_ip(0,-10)
        if pressed[pygame.K_l]: paddle2.move_ip(0,10)

        drawArena()
        drawPaddle(paddle1)
        drawPaddle(paddle2)
        drawBall(ball)
        ball = moveBall(ball, ballDirX, ballDirY)
        ballDirX = ballDirX * checkHitBall(ball, paddle1, paddle2, ballDirX)
        player_1_score, player_2_score = checkPointScored(paddle1, ball,player_1_score,player_2_score, ballDirX)
        ballDirX, ballDirY = checkForEdgeCollision(ball, ballDirX, ballDirY)
        display_score_1(player_1_score)
        display_score_2(player_2_score)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def moveBall(ball, ballDirX, ballDirY):
    ball.x += ballDirX
    ball.y += ballDirY
    return ball

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

def drawBall(ball):
    pygame.draw.rect(DISPLAYSURF, WHITE, ball)

def checkForEdgeCollision(ball, ballDirX, ballDirY):
    if ball.top == (LINETHICKNESS) or ball.bottom == (WINDOWHEIGHT - LINETHICKNESS):
        ballDirY = ballDirY * - 1
    if ball.left == (LINETHICKNESS) or ball.right == (WINDOWWIDTH - LINETHICKNESS):
        ballDirX = ballDirX * - 1
    return ballDirX, ballDirY

def checkHitBall(ball, paddle1, paddle2, ballDirX):
    if ballDirX == -1 and paddle1.right == ball.left and paddle1.top < ball.top and paddle1.bottom > ball.bottom:
        return -1
    elif ballDirX == 1 and paddle2.left == ball.right and paddle2.top < ball.top and paddle2.bottom > ball.bottom:
        return -1
    else: return 1

def checkPointScored(paddle1, ball,player_1_score, player_2_score, ballDirX):
    if ball.left == LINETHICKNESS:
        player_1_score += 7
    elif ball.right == WINDOWWIDTH - LINETHICKNESS:
        player_2_score += 7
    return player_1_score, player_2_score

def display_score_1(player_1_score):
    resultSurf = BASICFONT.render('%s' %(player_1_score), True, WHITE)
    resultRect = resultSurf.get_rect()
    resultRect.topleft = (WINDOWWIDTH - 300, 50)
    DISPLAYSURF.blit(resultSurf, resultRect)

def display_score_2(player_2_score):
    resultSurf = BASICFONT.render('%s' %(player_2_score), True, WHITE)
    resultRect = resultSurf.get_rect()
    resultRect.topleft = (300, 50)
    DISPLAYSURF.blit(resultSurf, resultRect)

if __name__ == '__main__':
    main()

# drawArena()
