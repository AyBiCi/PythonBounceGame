import pygame

pygame.init()

DISPLAY_X = 640
DISPLAY_Y = 480

surface = pygame.display.set_mode( (DISPLAY_X,DISPLAY_Y) )
pygame.display.set_caption("Bounce")

while True:
    surface.fill((0,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    pygame.display.update()