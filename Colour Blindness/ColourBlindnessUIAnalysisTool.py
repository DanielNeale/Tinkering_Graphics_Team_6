import pygame
pygame.init()

main_window = pygame.display.set_mode((1680, 1050))

# Sets all of the images which will be tinkered. I'm using separate images as
# I tried to use one but all of the different stages conflicted and produced
# incorrect images.

achro_image = pygame.image.load("cat.jpg").convert()
protanopia_image = pygame.image.load("cat.jpg").convert()
protanomaly_image = pygame.image.load("cat.jpg").convert()
deuteranopia_image = pygame.image.load("cat.jpg").convert()
deuteranomaly_image = pygame.image.load("cat.jpg").convert()
tritanopia_image = pygame.image.load("cat.jpg").convert()
tritanomaly_image = pygame.image.load("cat.jpg").convert()


# Main section of the code where it calls each individual function to tinker the image
# It then briefly displays it in the window to be checked and then saved to a file.

def main():
    tritanomaly()
    main_window.blit(tritanomaly_image, (0, 0))
    pygame.image.save(tritanomaly_image, "tritanomaly.jpg")
    pygame.display.update()

    tritanopia()
    main_window.blit(tritanopia_image, (0, 0))
    pygame.image.save(tritanopia_image, "tritanopia.jpg")
    pygame.display.update()

    deuteranomaly()
    main_window.blit(deuteranomaly_image, (0, 0))
    pygame.image.save(deuteranomaly_image, "deuteranomaly.jpg")
    pygame.display.update()

    deuteranopia()
    main_window.blit(deuteranopia_image, (0, 0))
    pygame.image.save(deuteranopia_image, "deuteranopia.jpg")
    pygame.display.update()

    protanomaly()
    main_window.blit(protanomaly_image, (0, 0))
    pygame.image.save(protanomaly_image, "protanomaly.jpg")
    pygame.display.update()

    protanopia()
    main_window.blit(protanopia_image, (0, 0))
    pygame.image.save(protanopia_image, "protanopia.jpg")
    pygame.display.update()

    achromatopsia()
    main_window.blit(achro_image, (0, 0))
    pygame.image.save(achro_image, "achromatopsia.jpg")
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


# These are all the functions to manipulate the images to be perceived as if you were colourblind
# Asides from the top one where I only had to find a greyscale all of these functions use an
# algorithm found here (https://github.com/MaPePeR/jsColorblindSimulator/blob/master/colorblind.js)
# which modifies the colours to the specification. It isn't perfect however it is very close and I
# believe for the purpose of the assignment it is suitable and gives at least a good idea on what
# the image would look like to someone with colourblindness.

def achromatopsia():
    for x in range(0, achro_image.get_width()):
        for y in range(0, achro_image.get_height()):
            current_pixel = achro_image.get_at((x, y))
            pixel_r = current_pixel[0]
            pixel_g = current_pixel[1]
            pixel_b = current_pixel[2]
            pixel_achro = int((pixel_r + pixel_g + pixel_b) / 3)
            current_pixel = (pixel_achro, pixel_achro, pixel_achro)
            achro_image.set_at((x, y), current_pixel)


def protanopia():
    for x in range(0, protanopia_image.get_width()):
        for y in range(0, protanopia_image.get_height()):
            current_pixel = protanopia_image.get_at((x, y))
            pixel_r = current_pixel[0]
            pixel_g = current_pixel[1]
            pixel_b = current_pixel[2]
            pixel_r = int((pixel_r * 56.667 / 100) + (pixel_g * 43.333 / 100) + (pixel_b * 0 / 100))
            pixel_g = int((pixel_r * 55.833 / 100) + (pixel_g * 44.167 / 100) + (pixel_b * 0 / 100))
            pixel_b = int((pixel_r * 0 / 100) + (pixel_g * 24.167 / 100) + (pixel_b * 75.833 / 100))
            current_pixel = (pixel_r, pixel_g, pixel_b)
            protanopia_image.set_at((x, y), current_pixel)


def protanomaly():
    for x in range(0, protanomaly_image.get_width()):
        for y in range(0, protanomaly_image.get_height()):
            current_pixel = protanomaly_image.get_at((x, y))
            pixel_r = current_pixel[0]
            pixel_g = current_pixel[1]
            pixel_b = current_pixel[2]
            pixel_r = int((pixel_r * 81.667 / 100) + (pixel_g * 18.333 / 100) + (pixel_b * 0 / 100))
            pixel_g = int((pixel_r * 33.333 / 100) + (pixel_g * 66.667 / 100) + (pixel_b * 0 / 100))
            pixel_b = int((pixel_r * 0 / 100) + (pixel_g * 12.5 / 100) + (pixel_b * 87.5 / 100))
            current_pixel = (pixel_r, pixel_g, pixel_b)
            protanomaly_image.set_at((x, y), current_pixel)


def deuteranopia():
    for x in range(0, deuteranopia_image.get_width()):
        for y in range(0, deuteranopia_image.get_height()):
            current_pixel = deuteranopia_image.get_at((x, y))
            pixel_r = current_pixel[0]
            pixel_g = current_pixel[1]
            pixel_b = current_pixel[2]
            pixel_r = int((pixel_r * 62.5 / 100) + (pixel_g * 37.5 / 100) + (pixel_b * 0 / 100))
            pixel_g = int((pixel_r * 70 / 100) + (pixel_g * 30 / 100) + (pixel_b * 0 / 100))
            pixel_b = int((pixel_r * 0 / 100) + (pixel_g * 30 / 100) + (pixel_b * 70 / 100))
            current_pixel = (pixel_r, pixel_g, pixel_b)
            deuteranopia_image.set_at((x, y), current_pixel)#


def deuteranomaly():
    for x in range(0, deuteranomaly_image.get_width()):
        for y in range(0, deuteranomaly_image.get_height()):
            current_pixel = deuteranomaly_image.get_at((x, y))
            pixel_r = current_pixel[0]
            pixel_g = current_pixel[1]
            pixel_b = current_pixel[2]
            pixel_r = int((pixel_r * 80 / 100) + (pixel_g * 20 / 100) + (pixel_b * 0 / 100))
            pixel_g = int((pixel_r * 25.833 / 100) +(pixel_g * 74.167 / 100) + (pixel_b * 0 / 100))
            pixel_b = int((pixel_r * 0 / 100) + (pixel_g * 14.167 / 100) + (pixel_b * 85.833 / 100))
            current_pixel = (pixel_r, pixel_g, pixel_b)
            deuteranomaly_image.set_at((x, y), current_pixel)


def tritanopia():
    for x in range(0, tritanopia_image.get_width()):
        for y in range(0, tritanopia_image.get_height()):
            current_pixel = tritanopia_image.get_at((x, y))
            pixel_r = current_pixel[0]
            pixel_g = current_pixel[1]
            pixel_b = current_pixel[2]
            pixel_r = int((pixel_r * 95 / 100) + (pixel_g * 5 / 100) + (pixel_b * 0 / 100))
            pixel_g = int((pixel_r * 0 / 100) + (pixel_g * 43.333 / 100) + (pixel_b * 56.667 / 100))
            pixel_b = int((pixel_r * 0 / 100) + (pixel_g * 47.5 / 100) + (pixel_b * 52.5 / 100))
            current_pixel = (pixel_r, pixel_g, pixel_b)
            tritanopia_image.set_at((x, y), current_pixel)


def tritanomaly():
    for x in range(0, tritanomaly_image.get_width()):
        for y in range(0, tritanomaly_image.get_height()):
            current_pixel = tritanomaly_image.get_at((x, y))
            pixel_r = current_pixel[0]
            pixel_g = current_pixel[1]
            pixel_b = current_pixel[2]
            pixel_r = int((pixel_r * 96.667 / 100) + (pixel_g * 3.333 / 100) + (pixel_b * 0 / 100))
            pixel_g = int((pixel_r * 0 / 100) + (pixel_g * 73.333 / 100) + (pixel_b * 26.667 / 100))
            pixel_b = int((pixel_r * 0 / 100) + (pixel_g * 18.333 / 100) + (pixel_b * 81.667 / 100))
            current_pixel = (pixel_r, pixel_g, pixel_b)
            tritanomaly_image.set_at((x, y), current_pixel)


main()
