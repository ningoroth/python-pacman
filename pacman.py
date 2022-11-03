import random
import pygame as pg

class Pacman:
    # Constructor
    def __init__(self, x, y):
        self.x = x # attribute
        self.y = y # attribute

    def move(self, direction):
            if direction == "left":
                self.x -= 5
            elif direction == "right":
                self.x += 5
            elif direction == "up":
                self.y -= 5
            elif direction == "down":
                self.y += 5

    def draw(self, direction):
        r = int((tick/2)%6)
        if direction == "left":
            screen.blit(pacmanImages[r], (self.x, self.y))
        elif direction == "right":
            screen.blit(pg.transform.rotate(pacmanImages[r],180), (self.x, self.y))
        elif direction == "up":
            screen.blit(pg.transform.rotate(pacmanImages[r],-90), (self.x, self.y))
        elif direction == "down":
            screen.blit(pg.transform.rotate(pacmanImages[r],90), (self.x, self.y))
        else:
            screen.blit(pacmanImages[0], (self.x, self.y))