import cv2
import numpy as np

def main():
    print("placeholder")

    img = cv2.imread("apollo.jpg")
    img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY) 
    row,col = img.shape
    kernel = noise_reduction(5,1)
    cv2.imshow('image', img)
    img = convolve(img, kernel)

    cv2.imshow('convolved image', img)
    cv2.waitKey(0)

def noise_reduction(size, sigma):
    size = size // 2
    x, y = np.mgrid[-size:size+1, -size:size+1]
    normal = 1 / (2.0 * np.pi * sigma**2)
    g =  np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
    return g
    

def non_max_suppression():
    print("Placeholder")

def gradient_calculation():
    print("placeholder")

def double_threshold():
    print("placeholder")

def hysteresis():
    print("placeholder")

def convolve(image, kernel):
  rkernel=np.rot90(kernel,2)
  output = np.zeros((1+image.shape[0]-kernel.shape[0],1+image.shape[1]-kernel.shape[1]), dtype=image.dtype)
  for i in range(0,output.shape[0]):
   for j in range(0,output.shape[1]):
    signal_patch = image[i:i+kernel.shape[0],j:j+kernel.shape[1]]
    tmp = (rkernel * signal_patch).sum()
    '''not really the best method to normalize the image'''
    output[i,j]=tmp
  return output

if __name__ == "__main__":
    main()
