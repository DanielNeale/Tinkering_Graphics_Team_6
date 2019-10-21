import cv2,sys,numpy

""" 
    Class with helper functions for removing red eyes from a photo 
    Original author: Satya Mallick(https://www.learnopencv.com/automatic-red-eye-remover-using-opencv-cpp-python/)
    
    All credit goes to original author. I have only put the code code into a Python module
    and also fixed an error where mean would stay as a float64. I fixed this by
    changing:
        mean = [:, :, numpy.newaxis]
    to
        mean = mean.astype(numpy.uint8)[:, :, numpy.newaxis]

    There is still an issue, however, where only one red eye is removed.
"""
def fillHoles(mask):
    """ Helper function that fills holes in a mask"""
    maskFloodfill = mask.copy()
    h, w = maskFloodfill.shape[:2]
    maskTemp = numpy.zeros((h+2, w+2), numpy.uint8)
    cv2.floodFill(maskFloodfill, maskTemp, (0, 0), 255)
    mask2 = cv2.bitwise_not(maskFloodfill)
    return mask2 | mask


def RemoveRedEyes(Image_Path,Cascade_Classifier_Path):
    """Remove red eyes from an image given it's directory, as-well as the directory to a valid HAAR cascade. Returns an image with the red eyes removed."""

    Image=cv2.imread(Image_Path,cv2.IMREAD_COLOR)
    HAAR_Cascade= cv2.CascadeClassifier(Cascade_Classifier_Path)


    Image_Output=Image.copy()

    """Detect eyes in the image using the HAAR cascade"""

    eyes = HAAR_Cascade.detectMultiScale(Image,scaleFactor=1.3, minNeighbors=4, minSize=(100, 100))
    mask=int(0)
    """Mask the eyes in the image"""
    for (x, y, w, h) in eyes:
        eye = Image[y:y+h, x:x+w]
        r = eye[:, :, 2]
        b = eye[:, :, 0]
        g = eye[:, :, 1]

        bg = cv2.add(b, g)

        mask = (r > 150) &  (r > bg)

        mask = mask.astype(numpy.uint8)*255
    
    mask=fillHoles(mask)
    mask=cv2.dilate(mask,None,anchor=(-1,-1),iterations=8,borderType=1,borderValue=1)

    """Calculate the mean channel by averaging the green and blue channels. Recall, bg = cv2.add(b, g)"""
    mean = bg / 2
    mask = mask.astype(numpy.bool)[:, :, numpy.newaxis]
    mean = mean.astype(numpy.uint8)[:, :, numpy.newaxis]
    
    """Copy the eye from the original image.""" 
    eyeOutput = eye.copy()
    """Copy the mean image to the output image.""" 
    numpy.copyto(eyeOutput, mean, where=mask)
    Image_Output[y:y+h,x:x+w,:]=eyeOutput

    return Image_Output
