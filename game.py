import pygame
import os

class GameObject(object):
    def __init__(self, textureName,location):
        self.surface = pygame.image.load(os.path.join('textures', textureName))
        self.location = location
    def render(self, screen):
        screen.blit(self.surface, self.location)
    def update(self):
        self.location[1] += 0.1

pygame.init()

DISPLAY_X = 640
DISPLAY_Y = 480

screen = pygame.display.set_mode( (DISPLAY_X, DISPLAY_Y) )
pygame.display.set_caption("Bounce")

obj = GameObject('bounce.png', [100,100] )

while True:
    screen.fill((0,255,255))

    obj.update()
    obj.render(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    pygame.display.update()