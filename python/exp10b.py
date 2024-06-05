\
import pygame
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400, 300))

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.circle(screen, (255, 255, 255), [100, 80], 10, 0)
    pygame.display.update()

    pygame.draw.circle(screen, (0, 0, 0), (100, 80), 10, 0)
    pygame.display.update()

    pygame.draw.circle(screen, (255, 255, 255), [150, 95], 10, 0)
    pygame.display.update()

    pygame.draw.circle(screen, (0, 0, 0), [150, 95], 10, 0)
    pygame.display.update()

    pygame.draw.circle(screen, (255, 255, 255), (200, 130), 10, 0)
    pygame.display.update()

    pygame.draw.circle(screen, (0, 0, 0), (200, 130), 10, 0)
    pygame.display.update()

    pygame.draw.circle(screen, (255, 255, 255), (250, 150), 10, 0)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()