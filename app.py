import cv2
import numpy as np
from scipy import ndimage
from customCanny import *

def main():
    
    for i in range(136):
        print(str(i+64) + "\n")
        # Read the image
        img = cv2.imread("./NoMask/img_nomask_"+ str(i+64) + ".jpg")
        img = cv2.resize(img, (500, 500))
        # Set the image to grayscale
        img = np.float32(cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY))
        img = img / img.max()
        # cv2.imshow('image', img)
        # cv2.waitKey(0)
        
        # Get the noised reduced image
        img = noise_reduction(img, 5, 1.5)
        # cv2.imshow('convolved image', img)
        # cv2.waitKey(0)
        
        # Get gradient calculated image
        g, slope = gradient_calculation(img)
        # cv2.imshow('gradient calculated image', g)
        # cv2.waitKey(0)
        
        # Non-Max Suppression
        img = non_max_suppression(g, slope)
        # cv2.imshow('non-max suppression image', img)
        # cv2.waitKey(0)

        # double-threshold Suppression
        img = double_threshold(img, 0.05, 0.15)
        # cv2.imshow('double-threshold image', img)
        # cv2.waitKey(0)

        # hy Suppression
        img = hysteresis(img)
        # cv2.imshow('hysteresis image', img)
        # cv2.waitKey(0)
        cv2.imwrite("./NoMaskEdge/img_edge_momask_" + str(i+64) + ".jpg", img)

if __name__ == "__main__":
    main()
