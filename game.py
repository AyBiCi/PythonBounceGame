import pygame
import os
import time
tiles = []

class Hitbox(object):
    def __init__(self, size, location):
        self.size = size
        self.bounceCoefficient = 0.5
        self.location = location
        self.maxLeft = location[0] - size/2
        self.maxRight = location[0] + size/2
        self.maxTop = location[1] - size/2
        self.maxBottom = location[1] + size/2
    def getBounceVector(self, hitbox):
        self.maxLeft = self.location[0] - self.size/2
        self.maxRight = self.location[0] + self.size/2
        self.maxTop = self.location[1] - self.size/2
        self.maxBottom = self.location[1] + self.size/2
        if (self.maxBottom >= hitbox.maxTop and self.maxRight >= hitbox.maxLeft and self.maxLeft <= hitbox.maxRight):
            print('vectorbounce')
            return [1*self.bounceCoefficient,-1*self.bounceCoefficient]
        return [1,1]

class GameObject(object):
    def __init__(self, textureName,location):
        self.surface = pygame.image.load(os.path.join('textures', textureName))
        self.location = location
    def render(self, screen):
        r = [self.location[0]-32, self.location[1]-32]
        screen.blit(self.surface, r)
    def update(self):
        pass

class Tile(GameObject):
    def __init__(self, size, location):
        GameObject.__init__(self, size, location)
        self.hitbox = Hitbox(64, self.location)

class Bounce(GameObject):
    def __init__(self, size, location):
        GameObject.__init__(self, size, location)
        self.velocityVector = [0,1]
        self.hitbox = Hitbox(64, self.location)
        self.gravity = 0.1
    def update(self):
        if abs(self.velocityVector[1]) > 0.1:
            self.velocityVector[1] += 0.1
        self.location[1] += self.velocityVector[1]
        self.location[0] += self.velocityVector[0]
        if abs(self.velocityVector[0]) < 0.1:
            self.velocityVector[0] = 0
            self.gravity = 0
        if abs(self.velocityVector[1]) < 0.1:
            self.velocityVector[1] = 0
            self.gravity = 0
        for tile in tiles:
            bounceVector = self.hitbox.getBounceVector(tile.hitbox)
            self.velocityVector[0] *= bounceVector[0]
            self.velocityVector[1] *= bounceVector[1]

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

DISPLAY_X = 640
DISPLAY_Y = 480

screen = pygame.display.set_mode( (DISPLAY_X, DISPLAY_Y) )
pygame.display.set_caption("Bounce")

bounce = Bounce('bounce.png', [100,100] )

def current_milli_time():
    return round(time.time() * 1000)

measured = 0

loadLevel('level1.lvl')

while True:
    
    screen.fill((0,255,255))

    
    for tile in tiles:
        tile.render(screen)

    bounce.update()
    bounce.render(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    time.sleep(0.01)
    pygame.display.update()