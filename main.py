import pygame
import sys
import random
from random import randint
import pickle

# config var
windowWidth = 400
windowHeight = 400
clock = pygame.time.Clock()

# display
screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Snake')

#colors
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)

# fonts
pygame.font.init()
font = pygame.font.SysFont("comicsans", 50)

# game
score = 0
gridSize = 20
gameSpeed = 7

# sprites
snakeSquares = []

class snake:
    def __init__(self, x, y, direction):
        self.x = x * gridSize
        self.y = y * gridSize
        self.direction = direction
    
    def drawSquare(self):
        pygame.draw.rect(screen, green, (self.x,self.y,gridSize, gridSize))

    def death(self):
        print("u died")

    def move(self):
        if self.direction == "left":
            self.x -= gridSize
        elif self.direction == "right":
            self.x += gridSize
        elif self.direction == "up":
            self.y -= gridSize
        elif self.direction == "down":
            self.y += gridSize
        
        if self.y < 0 or self.y >= windowHeight:
            self.death()
        elif self.x < 0 or self.x >= windowWidth:
            self.death()
        
    
    def changeDirection(self, direction):
        if self.direction == "up" and direction == "down":
            return
        elif self.direction == "down" and direction == "up":
            return
        elif self.direction == "left" and direction == "right":
            return
        elif self.direction == "right" and direction == "left":
            return
        else:
            self.direction = direction

class food:
    def __init__(self, x, y):
        self.x = x * gridSize
        self.y = y * gridSize
    
    def drawFood(self):
        pygame.draw.rect(screen, red, (self.x,self.y, gridSize, gridSize))

def showScore(score):
    score_label = font.render("Score: " + str(score),1,(255,255,255))
    screen.blit(score_label, (10, 10))

snakeSquares.append(snake(4,windowHeight/2/gridSize-1,"right"))

running = True
backlog = []

while running:

    # running thru events
    events = pygame.event.get()
    for event in events:
        # if x button pressed stop just break out of these loops
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                backlog.append("up")
            elif event.key == pygame.K_DOWN:
                backlog.append("down")
            elif event.key == pygame.K_LEFT:
                backlog.append("left")
            elif event.key == pygame.K_RIGHT:
                backlog.append("right")
    
    # if backlog has elements on it, then execute the first (every loop)
    if len(backlog) > 0:
        snakeSquares[0].changeDirection(backlog[0])
        del(backlog[0])
    print(backlog)

    snakeSquares[0].move()
    
    apple = food(10,10)

    # drawing
    pygame.draw.rect(screen, black, (0,0,windowWidth, windowHeight))
    snakeSquares[0].drawSquare()
    apple.drawFood()

    # update display
    clock.tick(gameSpeed)
    showScore(score)
    pygame.display.update()