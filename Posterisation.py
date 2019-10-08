import pygame

pic = pygame.image.load("cat.jpg")

main_window = pygame.display.set_mode(pic.get_rect().size)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    main_window.blit(pic, (0, 0))
    pygame.display.update()
