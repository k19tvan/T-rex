import pygame
import random

pygame.init()
pygame.mixer.init()

# set var
width = 800
height = 400
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# dinosaur
trex_width, trex_height = 40, 40
trex_x, trex_y = 50, height - trex_height - 10 
trex_v = 0
gravity = 1
jump_strength = -15
is_jumping = False
trex_image = pygame.transform.scale(pygame.image.load('dinosaur.png'), (trex_width, trex_height))

# thorn
thorn_width, thorn_height = 20, 40
thorn_x = width
thorn_y = height - thorn_height - 10
thorn_v = 5
thorn_image = pygame.transform.scale(pygame.image.load('pipe.png'), (thorn_width, thorn_height))

# score
score = 0

# loop
running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping:
        is_jumping = True
        trex_v = jump_strength  
        
    if is_jumping:
        trex_y += trex_v
        trex_v += gravity
        if trex_y >= height - trex_height -10:
            trex_y = height - trex_height -10
            is_jumping = False
    
    thorn_x -= thorn_v
    if thorn_x < 0:
        thorn_x = width
        score += 1
    
    if trex_x < thorn_x + thorn_width and trex_x + trex_width > thorn_x and trex_y + trex_height > thorn_y:
        running = False

    screen.fill(WHITE)  
    # pygame.draw.rect(screen, BLACK, (trex_x, trex_y, trex_width, trex_height))
    screen.blit(trex_image, (trex_x, trex_y))
    screen.blit(thorn_image, (thorn_x, thorn_y))    
    pygame.display.flip()
    

# Endloop
pygame.quit()
            