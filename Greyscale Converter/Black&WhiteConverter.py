import pygame
from pygame.locals import*
from PIL import Image
import numpy as np
from scipy import ndimage
import matplotlib.pyplot
from scipy import misc


from PIL import Image

pygame.init()
img = Image.open('PaidInFull.jpg').convert('LA')
img.save('greyscale.png')
screen = pygame.display.set_mode((355, 355))
pygame.display.set_caption("Black & White Converter")

image = pygame.image.load('greyscale.png').convert()

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

screen.blit(background, (0, 0))
screen.blit(image, (225, 225))
pygame.display.flip()


while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))
    screen.blit(image, (0, 0))
    pygame.display.flip()