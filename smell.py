import pygame, sys
from pygame.locals import *

FPS = 1000

WINDOWWIDTH = 700
WINDOWHEIGHT = 700

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

    playerThreePosition = (WINDOWWIDTH - PADDLESIZE)/2
    playerFourPosition = (WINDOWWIDTH - PADDLESIZE)/2

    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 20
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    player_1_score = 0
    player_2_score = 0

    left_paddle = pygame.Rect(PADDLEOFFSET, playerOnePosition, LINETHICKNESS, PADDLESIZE)
    right_paddle = pygame.Rect(WINDOWWIDTH-PADDLEOFFSET-LINETHICKNESS, playerTwoPosition, LINETHICKNESS, PADDLESIZE)

    top_paddle = pygame.Rect(playerThreePosition, PADDLEOFFSET, PADDLESIZE, LINETHICKNESS)
    bottom_paddle = pygame.Rect(playerFourPosition,WINDOWHEIGHT-PADDLEOFFSET-LINETHICKNESS, PADDLESIZE, LINETHICKNESS)

    ball = pygame.Rect(ballX, ballY, LINETHICKNESS, LINETHICKNESS)

    ballDirX = -3 ## -1 = left 1 = right
    ballDirY = -3 ## -1 = up 1 = down



    drawArena()
    drawPaddle(left_paddle)
    drawPaddle(right_paddle)
    drawPaddle(top_paddle)
    drawPaddle(bottom_paddle)
    drawBall(ball)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_q]: left_paddle.move_ip(0,-10)
        if pressed[pygame.K_a]: left_paddle.move_ip(0,10)
        if pressed[pygame.K_p]: right_paddle.move_ip(0,-10)
        if pressed[pygame.K_l]: right_paddle.move_ip(0,10)

        if pressed[pygame.K_m]: top_paddle.move_ip(10,0)
        if pressed[pygame.K_n]: top_paddle.move_ip(-10,0)
        if pressed[pygame.K_x]: bottom_paddle.move_ip(-10,0)
        if pressed[pygame.K_c]: bottom_paddle.move_ip(10,0)

        drawArena()
        drawPaddle(left_paddle)
        drawPaddle(right_paddle)
        drawPaddle(top_paddle)
        drawPaddle(bottom_paddle)
        drawBall(ball)
        ball = moveBall(ball, ballDirX, ballDirY)
        ballDirX = ballDirX * checkHitBall(ball, left_paddle, right_paddle, ballDirX)
        ballDirY = ballDirY * checkHitBallY(ball, top_paddle, bottom_paddle, ballDirY)
        player_1_score, player_2_score = checkPointScored(left_paddle, ball,player_1_score,player_2_score, ballDirX)
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
    # pygame.draw.line(DISPLAYSURF, WHITE, ((WINDOWWIDTH/2),0),((WINDOWWIDTH/2),WINDOWHEIGHT), (LINETHICKNESS/4))

def drawPaddle(paddle):
    if paddle.bottom > WINDOWHEIGHT - LINETHICKNESS:
        paddle.bottom = WINDOWHEIGHT - LINETHICKNESS
    elif paddle.top < LINETHICKNESS:
        paddle.top = LINETHICKNESS
    elif paddle.left < LINETHICKNESS:
        paddle.left = LINETHICKNESS
    elif paddle.right > WINDOWWIDTH - LINETHICKNESS:
        paddle.right = WINDOWWIDTH - LINETHICKNESS
    pygame.draw.rect(DISPLAYSURF, WHITE, paddle)

def drawBall(ball):
    pygame.draw.rect(DISPLAYSURF, WHITE, ball)

def checkForEdgeCollision(ball, ballDirX, ballDirY):
    if ball.top == (LINETHICKNESS) or ball.bottom == (WINDOWHEIGHT - LINETHICKNESS):
        ballDirY = ballDirY * - 1
    if ball.left == (LINETHICKNESS) or ball.right == (WINDOWWIDTH - LINETHICKNESS):
        ballDirX = ballDirX * - 1
    return ballDirX, ballDirY

def checkHitBall(ball, left_paddle, right_paddle, ballDirX):
    if ballDirX == -1 and left_paddle.right == ball.left and left_paddle.top < ball.top and left_paddle.bottom > ball.bottom:
        return -1
    elif ballDirX == 1 and right_paddle.left == ball.right and right_paddle.top < ball.top and right_paddle.bottom > ball.bottom:
        return -1
    else: return 1

def checkHitBallY(ball, top_paddle, bottom_paddle, ballDirY):
    if ballDirY == 1 and bottom_paddle.top == ball.bottom and bottom_paddle.right < ball.right and bottom_paddle.left > ball.left:
        return -1
    elif ballDirY == -1 and top_paddle.bottom == ball.top and top_paddle.left < ball.left and top_paddle.right > ball.right:
        return -1
    else: return 1

def checkPointScored(left_paddle, ball,player_1_score, player_2_score, ballDirX):
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
