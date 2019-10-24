import pygame, sys, random
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)

# set up the window
DISPLAYSURF = pygame.display.set_mode((1920, 1080), 0, 32)
pygame.display.set_caption('Random Monster Generator')

DISPLAYSURF.fill(WHITE)

fHead = pygame.image.load('frankHead.png')
fBody = pygame.image.load('frankBody.png')
fLegs = pygame.image.load('frankLegs.png')
mHead = pygame.image.load('mummyHead.png')
mBody = pygame.image.load('mummyBody.png')
mLegs = pygame.image.load('mummyLegs.png')
vHead = pygame.image.load('vampHead.png')
vBody = pygame.image.load('vampBody.png')
vLegs = pygame.image.load('vampLegs.png')

heads = [fHead, mHead, vHead]
bodies = [fBody, mBody, vBody]
legs = [fLegs, mLegs, vLegs]

DISPLAYSURF.blit(heads[random.randrange(0, 2, 1)], (0, 0))
DISPLAYSURF.blit(bodies[random.randrange(0, 2, 1)], (0, 5))
DISPLAYSURF.blit(legs[random.randrange(0, 2, 1)], (0, 10))

# the main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()