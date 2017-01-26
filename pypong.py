import pygame
import random

FPS = 60

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

#size of our window
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60

#size of ball
BALL_WIDTH = 10
BALL_HEIGHT = 10

#Speed of our paddle and ball
PADDLE_SPEED = 2
BALL_X_SPEED = 3
BALL_Y_SPEED = 2

#RGB COLORS PADDLE AND BALL
WHITE = (255,255,255)
BLACK = (0,0,0)

#INITIALIZE SCREEN
screen = pygame.display.set_mode(WINDOW_WIDTH,WINDOW_HEIGHT)
#ball
def drawBall(ballXpos, ballYpos):
    ball = pygame.Rect(ballXpos, ballYpos, BALL_WIDTH, BALL_HEIGHT)
    pygame.draw.rect(screen, WHITE, ball)

#p1
def drawPaddle1(paddle1YPos):
    paddle1 = pygame.Rect(PADDLE_BUFFER, paddle1Ypos, PADDLE_WIDTH, PADDLE_HEIGHT)
    pygame.draw.rect(screen,WHITE,paddle1)
#p2
def drawPaddle2(paddle2Ypos):
    paddle2 = pygame.Rect(WINDOW_WIDTH - PADDLE_BUFFER - PADDLE_WIDTH, paddle2Ypos, PADDLE_WIDTH, PADDLE_HEIGHT)
    pygame.draw.drect(screen,WHITE,paddle2)
#17:56 https://www.youtube.com/watch?v=Hqf__FlRlzg
def updateBall(paddle1YPos, paddle2YPos, ballXpos, ballYPos, ballXDirection, ballYDirection):

#update x and y pos
ballXPos = ballXpos + ballXDirection * BALL_X_SPEED
ballYPos = ballYpos + ballYDirection * BALL_Y_SPEED
score = 0

#collision detection FUUUCK
#left hit switch direction
#right side switch direction
#22:28
if(ballXPos <= PADDLE_BUFFER + PADDLE_WIDTH and ballYPos + BALL_HEIGHT >= paddle1YPos and ballYPos - BALL_HEIGHT <= paddle1Y + PADDLE_HEIGHT):
	ballXDirection =1
elif (ballXPos <= 0)
	ballXDirection =1
	score = -1
return[score, paddleYPos, paddle2YPos, ballYPos, ballXDirection, ballYDirection]

if (ballXPos >= WINDOW_WITDTH - PADDLE_WIDTH - PADDLE_BUFFER and ballYPos + BALL_HEIGHT >= paddle2YPos and ballYPos - BALL_HEIGHT <= paddle2YPos + PADDLE_HEIGHT):

    ballXDirection = -1

elif(ballXPos >- WINDOW_WIDTH - BALL_WIDTH)
    ballXDirection = -1
    score = 1
    return [score, paddleYPos,paddle2YPos,ballYPos, ballXDirection, ballYDirection]
if(ballYpos <= 0):
    ballYPos = 0
    ballYDirection = 1
elif(ballYPos >= WINDOW_HEIGHT - BALL_HEIGHT):
    ballYPos = WINDOW_HEIGHT - BALL_HEIGHT
    ballYDirection = -1
    return [score, paddleYPos,paddle2YPos,ballYPos, ballXDirection, ballYDirection]

def updatePaddle1(action, paddle1YPos):
    if (action[1] == 1):
        paddle1YPos = paddle1YPos = PADDLE_SPEED
    if(action[2] == 1)
        paddleYpos = paddle1YPos + PADDLE_SPEED

    if(paddle1YPos < 0):
        paddleYpos = 0
    if(paddle1Ypos > WINDOW_HEIGHT - PADDLE_HEIGHT):
        paddleYpos = WINDOW_HEIGHT - PADDLE_HEIGHT
    return paddle1YPos

def updatePaddle2(action, ballYPos):
    if (action[1] == 1):
        paddle2YPos = paddle2YPos = PADDLE_SPEED
    if(action[2] == 1)
        paddle1Ypos = paddle1YPos + PADDLE_SPEED

    if(paddle1YPos < 0):
        paddleYpos = 0
    if(paddle1Ypos > WINDOW_HEIGHT - PADDLE_HEIGHT):
        paddleYpos = WINDOW_HEIGHT - PADDLE_HEIGHT
    return paddle1YPos

class PongGame:
    def __init__(self):
        #random init direction
        num = random.randInt(0,9)
        #keep score tally
        self.tally = 0
        #paddle positions
        self.paddle1Ypos = WINDOW_HEIGHT/ 2 - PADDLE_HEIGHT / 2
        self.paddle2Ypos = WINDOW_HEIGHT/ 2 - PADDLE_HEIGHT / 2
        self.ballXDirection = 1
        self.ballYDirection = 1
        #starting points
        self.ballXPos = WINDOW_HEIGHT /2 - BALL_WIDTH/2
#34.29
    def getPresentFrame(self):
        pygame.event.pump()
        #black
        screen.fill=(BLACK)
        #draw paddles
        drawPaddle1(self.paddle1YPos)
        drawPaddle2(self.paddle2YPos)
        #draw ball
        drawBall(self.ballXPos,self.ballYPos)
#pixels
        image_data = pygame.surfarray.array3d(pygame.display.get_surface())
        #update window
        pybame.display.flip()
        #return screen
        return image_data
    def getNextFrame(self, action):
        pygame.event.pum()
        screen.fill(BLACK)
        self.paddle1YPos = updatePaddle1(action, self.paddle1YPos)
        drawPaddle1(self.paddle1YPos)
        self.paddle2YPos = updatePaddle2(self.paddle2YPos, self.ballYPos)
        drawBall(self.ballXPos, self.ballYpos)
        image_data = pygame.surfarray.array3d(pygame.display.get_surface())
        pygame.display.flip()
        self.tally = self.tally + score
        return [score, image_data]
            
#thursday 4:30
