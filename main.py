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

# sprites
snakeSquares = []

class snake:
    def __init__(self, x, y, direction):
        self.x = x * gridSize
        self.y = y * gridSize
        self.direction = direction
    
    def drawSquare(self):
        pygame.draw.rect(screen, green, (self.x,self.y,gridSize, gridSize))

    def move(self, direction):
        if direction == "left":
            self.x -= gridSize
        if direction == "right":
            self.x += gridSize
        if direction == "up":
            self.y -= gridSize
        if direction == "down":
            self.y += gridSize
        self.direction = direction


class food:
    def __init__(self, x, y):
        self.x = x
        self.y = y

running = True

snakeSquares.append(snake(5,5,"left"))

while running:

    # running thru events
    events = pygame.event.get()
    for event in events:
        # if x button pressed stop just break out of these loops
        if event.type == pygame.QUIT:
            running = False
        # if key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snakeSquares[0].move("up")
            if event.key == pygame.K_DOWN:
                snakeSquares[0].move("down")
            if event.key == pygame.K_LEFT:
                snakeSquares[0].move("left")
            if event.key == pygame.K_RIGHT:
                snakeSquares[0].move("right")
    
    # background
    pygame.draw.rect(screen, black, (0,0,windowWidth, windowHeight))

    # snake
    snakeSquares[0].drawSquare()

    # score
    score_label = font.render("Score: " + str(score),1,(255,255,255))
    screen.blit(score_label, (10, 10))

    # update display
    pygame.display.update()