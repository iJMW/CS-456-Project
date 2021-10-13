import cv2
import numpy as np
from scipy import ndimage

def main():
    print("placeholder")

    img = cv2.imread("apollo.jpg")
    img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY) 
    row,col = img.shape
    kernel = noise_reduction(5,1)
    cv2.imshow('image', img)
    img = ndimage.filters.convolve(img, kernel)

    cv2.imshow('convolved image', img)
    cv2.waitKey(0)

def noise_reduction(size, sigma):
    size = size // 2
    x, y = np.mgrid[-size:size+1, -size:size+1]
    normal = 1 / (2.0 * np.pi * sigma**2)
    g =  np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
    return g
    

def non_max_suppression(img):
    Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
    Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)

    Ix = ndimage.filters.convolve(img, Kx)
    Iy = ndimage.filters.convolve(img, Ky)

    G = np.hypot(Ix, Iy)
    G = G / G.max() * 255
    theta = np.arctan2(Iy, Ix)
    
    return (G, theta)

def gradient_calculation():
    print("placeholder")

def double_threshold():
    print("placeholder")

def hysteresis():
    print("placeholder")



if __name__ == "__main__":
    main()
