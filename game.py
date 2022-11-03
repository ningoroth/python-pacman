# Pac-Man clone made for learning/teaching
# https://www.pygame.org/docs/

import time
import random
import pygame as pg
from ghost import Ghost
from pacman import Pacman

## Load images ##
pacmanImages = []
for i in range(6):
    img = pg.image.load(f"images/pacmanImages/pacman_{i}.png")
    img = pg.transform.scale(img, (32,32))
    pacmanImages.append(img)

blueGhost = []
for i in range(4):
    img = pg.image.load(f"images/ghostsImages/blue_{i}.png")
    img = pg.transform.scale(img, (32,32))
    blueGhost.append(img)

orangeGhost = []
for i in range(4):
    img = pg.image.load(f"images/ghostsImages/orange_{i}.png")
    img = pg.transform.scale(img, (32,32))
    orangeGhost.append(img)

pinkGhost = []
for i in range(4):
    img = pg.image.load(f"images/ghostsImages/pink_{i}.png")
    img = pg.transform.scale(img, (32,32))
    pinkGhost.append(img)

redGhost = []
for i in range(4):
    img = pg.image.load(f"images/ghostsImages/red_{i}.png")
    img = pg.transform.scale(img, (32,32))
    redGhost.append(img)

## Level ##
level = []
with open('level.txt', 'r') as level_file:
    for r, line in enumerate(level_file):
        row = []
        for c, char in enumerate(line):
            if char == "#":
                row.append("#")
            elif char == "p":
                y = r*32
                x = c*32
                row.append(" ")
            else:
                row.append(" ")

        level.append(row)

num_rows = len(level)
num_cols = len(level[0])

## Screen setup ##
pg.init()
width = num_cols * 30
height = num_rows * 30
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Pac-Man")
pg.display.set_icon(pacmanImages[1])

pacman = Pacman(x,y)

ghost = Ghost(width/2, height/2)
ghost2 = Ghost(width/2, height/2)
ghost3 = Ghost(width/2, height/2)
ghost4 = Ghost(width/2, height/2)

direction = " "
ghostDirection = " "

running = True
tick = 0
while running:

    # Event loop
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
        
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_a or event.key == pg.K_LEFT:
                direction = "left"
            elif event.key == pg.K_d or event.key == pg.K_RIGHT:
                direction = "right"
            elif event.key == pg.K_w or event.key == pg.K_UP:
                direction = "up"
            elif event.key == pg.K_s or event.key == pg.K_DOWN:
                direction = "down"
            elif event.key == pg.K_ESCAPE:
                running = False
    
    ## Movement ##
    pacman.move(direction)

    ghost.move(ghostDirection)
    ghost2.move(ghostDirection)
    ghost3.move(ghostDirection)
    ghost4.move(ghostDirection)

    # Draw level #
    screen.fill((0,0,0))
    for r, row in enumerate(level):
        for c, tile in enumerate(row):
            left = c*32
            top = r*32
            if tile == "#":
                pg.draw.rect(screen, (20,20,220), pg.Rect(left+1, top+1, 30,30), 1)

    # Draw
    pacman.draw(direction)

    ghost.draw()
    ghost2.draw()
    ghost3.draw()
    ghost4.draw()

    # Update screen
    pg.display.flip()

    # Framerate (limit by doing nothing)
    tick += 1
    time.sleep(0.05)