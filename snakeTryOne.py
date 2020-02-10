import pygame, sys
import random

pygame.init()
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Tim's Snake")


run = True


while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()




    pygame.draw.rect(window, (0, 250, 0),(10, 10, 10, 10))
    pygame.display.update()


pygame.quit()
