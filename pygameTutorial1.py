import pygame, sys
pygame.init() #initializes module


win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")
x = 150
y = 150
width = 50 
height = 50
vel = 5

#application loop needed to keep the window open
run = True
while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
"""while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit"""
