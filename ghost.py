import random
import pygame as pg

class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, ghostDirection):
        if ghostDirection == "left":
            self.x -= random.randint(-10, 10)
        elif ghostDirection == "right":
            self.x += random.randint(-10, 10)
        elif ghostDirection == "up":
            self.y -= random.randint(-10, 10)
        elif ghostDirection == "down":
            self.y += random.randint(-10, 10)
        
    
    def draw(self):
        global ghostDirection
        ghostDirection = random.choice(["left", "right", "up", "down"])
        r = int((tick/2)%4)
        if ghostDirection == "right":
            screen.blit(blueGhost[0], (self.x, self.y))
        elif ghostDirection == "up":
            screen.blit(blueGhost[1], (self.x, self.y))
        elif ghostDirection == "left":
            screen.blit(blueGhost[2], (self.x, self.y))
        elif ghostDirection == "down":
            screen.blit(blueGhost[3], (self.x, self.y))
        else:
            screen.blit(blueGhost[0], (self.x, self.y))