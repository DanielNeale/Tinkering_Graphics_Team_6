import sys, pygame, cv2, math, numpy,RedEye

"""
    Author: Bradley Bath
    Description: Calls RedEye.RemoveRedEyes, saves output image, and then displays it via pygame.

    Current issues:

    Red eye remover only removes one red eye on reference image
"""

pygame.init()      
surface_sz = 900

main_surface = pygame.display.set_mode((surface_sz, surface_sz))

IMG_PATH=r"C:\Users\badfi\Pictures\RedEye.png"
CASCADE_PATH=r"C:\Users\badfi\Pictures\haarcascade_eye.xml"

cv2.imwrite(r"C:\Users\badfi\Documents\Python Scripts\RedEyeRemoved.png",RedEye.RemoveRedEyes(IMG_PATH,CASCADE_PATH))

Removed=pygame.image.load(r"C:\Users\badfi\Documents\Python Scripts\RedEyeRemoved.png")

while True:
    ev = pygame.event.poll()   
    if ev.type == pygame.QUIT:  
        break                  

    main_surface.fill((0, 200, 255))
    main_surface.blit(Removed,(0,0))
    pygame.display.flip()

pygame.quit()