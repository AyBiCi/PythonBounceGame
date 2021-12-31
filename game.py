import pygame
import os
import time

class GameObject(object):
    def __init__(self, textureName,location):
        self.surface = pygame.image.load(os.path.join('textures', textureName))
        self.location = location
    def render(self, screen):
        screen.blit(self.surface, self.location)
    def update(self):
        pass

class Tile(GameObject):
    pass

class Bounce(GameObject):
    def update(self):
        self.location[1] += 1

tiles = []
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
    time.sleep(0.1)
    pygame.display.update()