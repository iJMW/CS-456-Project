import cv2
import numpy as np
from scipy import ndimage
from customCanny import *

def main():
    # Read the image
    img = cv2.imread("./Images/mask3.jpg")
    # Set the image to grayscale
    img = np.float32(cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY))
    img = img / img.max()
    cv2.imshow('image', img)
    cv2.waitKey(0)
    
    # Get the noised reduced image
    img = noise_reduction(img, 5, 1.5)
    cv2.imshow('convolved image', img)
    cv2.waitKey(0)
    
    # Get gradient calculated image
    g, slope = gradient_calculation(img)
    cv2.imshow('gradient calculated image', g)
    cv2.waitKey(0)
    
    # Non-Max Suppression
    img = non_max_suppression(g, slope)
    cv2.imshow('non-max suppression image', img)
    cv2.waitKey(0)

    # double-threshold Suppression
    img = double_threshold(img, 0.05, 0.15)
    cv2.imshow('double-threshold image', img)
    cv2.waitKey(0)

    # hy Suppression
    img = hysteresis(img)
    cv2.imshow('hysteresis image', img)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
