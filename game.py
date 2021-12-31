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

pygame.init()

DISPLAY_X = 640
DISPLAY_Y = 480

screen = pygame.display.set_mode( (DISPLAY_X, DISPLAY_Y) )
pygame.display.set_caption("Bounce")

bounce = Bounce('bounce.png', [100,100] )

def current_milli_time():
    return round(time.time() * 1000)

tiles = []
for i in range(5):
    tile = Tile('kafelek.png', [64*i,64])
    tiles.append(tile)

measured = 0
while True:
    
    screen.fill((0,255,255))

    bounce.update()
    bounce.render(screen)

    for tile in tiles:
        tile.render(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    time.sleep(0.1)
    pygame.display.update()