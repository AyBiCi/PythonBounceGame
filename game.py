import pygame
import os
import time
from math import sqrt

tiles = []

camera = [100, 0]

DISPLAY_X = 640
DISPLAY_Y = 480

screen = pygame.display.set_mode( (DISPLAY_X, DISPLAY_Y) )

class Hitbox(object):
    def __init__(self, size, location):
        self.location = location
        self.size = size
        self.bounceCoefficient = 0.6
        self.updateMaxes()
    def getBounceVector(self, hitbox):
        self.updateMaxes()
        if (self.maxBottom >= hitbox.maxTop and self.maxTop <= hitbox.maxBottom and self.maxRight >= hitbox.maxLeft and self.maxLeft <= hitbox.maxRight):
            print('vectorbounce')
            return [1*self.bounceCoefficient,-1*self.bounceCoefficient]
        return [1,1]
    def render(self, screen):
        color = (0,255,0)
        pygame.draw.circle(screen, color, [self.maxLeft + camera[0], self.location[1] + camera[1] ], 3)
        pygame.draw.circle(screen, color, [self.maxRight + camera[0], self.location[1]+ camera[1] ] , 3)
        pygame.draw.circle(screen, color, [self.location[0] + camera[0], self.maxTop + camera[1]], 3)
        pygame.draw.circle(screen, color, [self.location[0] + camera[0], self.maxBottom + camera[1]] , 3)

    def updateMaxes(self):
        self.maxLeft = self.location[0] - self.size/2
        self.maxRight = self.location[0] + self.size/2
        self.maxTop = self.location[1] - self.size/2
        self.maxBottom = self.location[1] + self.size/2

class GameObject(object):
    def __init__(self, textureName,location):
        self.surface = pygame.image.load(os.path.join('textures', textureName))
        self.location = location
    def render(self, screen):
        r = [self.location[0]-32 + camera[0], self.location[1]-32 + camera[1]]
        screen.blit(self.surface, r)
    def update(self):
        pass

class Tile(GameObject):
    def __init__(self, size, location):
        GameObject.__init__(self, size, location)
        self.hitbox = Hitbox(64, self.location)
    def render(self, screen):
        GameObject.render(self, screen)
        self.hitbox.render(screen)

class Bounce(GameObject):
    def __init__(self, size, location):
        GameObject.__init__(self, size, location)
        self.velocityVector = [20,1]
        self.hitbox = Hitbox(64, self.location)
        self.gravity = 0.2
    def update(self):
        if abs(self.velocityVector[1]) < 0.1:
            self.velocityVector[1] += self.gravity
        else:
            self.velocityVector[1] += self.gravity
        
        
        for tile in tiles:
            bounceVector = self.hitbox.getBounceVector(tile.hitbox)
            if(bounceVector[1] != 1):
                self.location[1] = tile.hitbox.location[1] - 63
                if(self.velocityVector[1] < 0.3):
                    self.velocityVector[1] = 0
            self.velocityVector[0] *= bounceVector[0]
            self.velocityVector[1] *= bounceVector[1]

        
        self.location[1] += self.velocityVector[1]
        self.location[0] += self.velocityVector[0]
    def render(self, screen):
        GameObject.render(self, screen)
        self.hitbox.render(screen)


def loadLevel(levelName):
    levelFile = open(os.path.join('levels', levelName), 'r')
    levelLines = levelFile.readlines()

    x = 0
    y = 0

    for line in levelLines:
        for c in line:
            print("x: "+str(x)+" y: "+str(y))
            if c == '1':
                print("added tile on: x"+str(64*x)+" y: "+str(64*y))
                tile = Tile('kafelek.png', [64*y,64*x])
                tiles.append(tile)
            y+=1
        x+=1
        y=0

pygame.init()




pygame.display.set_caption("Bounce")

bounce = Bounce('bounce.png', [100,100] )

def current_milli_time():
    return round(time.time() * 1000)

measured = 0

loadLevel('level1.lvl')

addVector = [0,0]
horizontalSpeed = 3


while True:
    
    screen.fill((0,255,255))

    
    for tile in tiles:
        tile.render(screen)

    bounce.update()
    camera = [bounce.location[0]*-1 + DISPLAY_X/2 , bounce.location[1] *-1 + DISPLAY_Y/2 + 120]
    bounce.render(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                addVector[0] = horizontalSpeed
 
            if event.key == pygame.K_LEFT:
                addVector[0] = -horizontalSpeed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                addVector[0] = 0

    bounce.velocityVector[0] += addVector[0]
    time.sleep(0.01)
    pygame.display.update()