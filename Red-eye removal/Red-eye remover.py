import sys, pygame, cv2, math, numpy,RedEye

"""
    Author: Bradley Bath
    Description: Calls RedEye.RemoveRedEyes, saves output image, and then displays it via pygame.

    Current issues:

    Only removes one red eye on reference image
"""

pygame.init()      
surface_sz = 900

OUTPUT_DIRECTORY=r"C:\Users\badfi\Documents\Python Scripts\RedEyeRemoved.png"

MAIN_SURFACE = pygame.display.set_mode((surface_sz, surface_sz))

IMG_PATH=r"C:\Users\badfi\Pictures\RedEye.png"

CASCADE_PATH=r"C:\Users\badfi\Pictures\haarcascade_eye.xml"

#Write the image returned by RedEye.RemoveRedEyes to the disk. Change output_directory to a valid path on your PC.
cv2.imwrite(OUTPUT_DIRECTORY,RedEye.RemoveRedEyes(IMG_PATH,CASCADE_PATH))

#Load the image we just writ to the disk with pygame
FINAL_OUTPUT=pygame.image.load(OUTPUT_DIRECTORY)

while True:
    ev = pygame.event.poll()   
    if ev.type == pygame.QUIT:  
        break                  

    MAIN_SURFACE.fill((0, 200, 255))
    #Display the final image
    MAIN_SURFACE.blit(FINAL_OUTPUT,(0,0))
    pygame.display.flip()

pygame.quit()