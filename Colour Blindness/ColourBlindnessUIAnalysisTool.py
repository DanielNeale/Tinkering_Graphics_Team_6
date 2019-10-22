import pygame
import time
pygame.init()

main_window = pygame.display.set_mode((1680, 1050))
image = pygame.image.load("cat.jpg").convert()

achro_image = image
protanopia_image = image


def main():
    protanopia()
    main_window.blit(protanopia_image, (0, 0))
    pygame.image.save(protanopia_image, "protanopia.jpg")
    pygame.display.update()

    time.sleep(.5)
    main_window.fill((0, 0, 0))

    achromatopsia()
    main_window.blit(achro_image, (0, 0))
    pygame.image.save(achro_image, "achromatopsia.jpg")
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


def achromatopsia():
    for x in range(0, achro_image.get_width()):
        for y in range(0, achro_image.get_height()):
            current_pixel = achro_image.get_at((x, y))
            PIXEL_R = current_pixel[0]
            PIXEL_G = current_pixel[1]
            PIXEL_B = current_pixel[2]
            PIXEL_GREY = int((PIXEL_R + PIXEL_G + PIXEL_B) / 3)
            current_pixel = (PIXEL_GREY, PIXEL_GREY, PIXEL_GREY)
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


main()
