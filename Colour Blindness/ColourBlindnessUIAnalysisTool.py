import pygame
pygame.init()

main_window = pygame.display.set_mode((1680, 1050))
image = pygame.image.load("cat.jpg").convert()

achro_image = image
protanopia_image = image


def main():
    achromatopsia()
    main_window.blit(achro_image, (0, 0))
    pygame.image.save(achro_image, "achromatopsia.jpg")

    protanopia()
    main_window.blit(protanopia_image, (0, 0))
    pygame.image.save(protanopia_image, "protanopia.jpg")
    print("complete")


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


main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
