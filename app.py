import cv2
import numpy as np

def main():
    print("placeholder")

def noise_reduction():
    print("placeholder")

#Check angle parameter?
def non_max_suppression(img, angleDirection):
    #Gets the size of the image
    (row, col) = img.Shape
    #Creates a matrix of zeros
    nonMaxMatrix = np.zeros(row, col)

    #Iterates over all the pixels
    for i in range(1, row-1):
        for j in range(1, col-1):
            #Assigns the neighboring pixels adjacent to the current pixel
            prevPixel = img[i][j]
            nextPixel = img[i][j]

            #Checks the pixels on the left and right
            if((0 <= angleDirection[i][j] < np.pi/4) or (7*np.pi/4 <= angleDirection[i][j] < 2*np.pi)):
                prevPixel = img[i, j-1]
                nextPixel = img[i, j+1]
            #Checks the pixels on the top right and bottom left
            elif((np.pi/4 <= angleDirection[i][j] < np.pi/2) or (5*np.pi/4 <= angleDirection[i][j] < 3*np.pi/2)):
                prevPixel = img[i+1, j-1]
                nextPixel = img[i-1, j+1]
            #Checks the pixels on the top middle and bottom middle
            elif((np.pi/2 <= angleDirection[i][j] < 3*np.pi/4) or (3*np.pi/2 <= angleDirection[i][j] < 7*np.pi/4)):
                prevPixel = img[i-1, j-1]
                nextPixel = img[i+1, j+1]
            #Checks the pixels on the top left and bottom right
            #Default case
            else:
                prevPixel = img[i-1, j-1]
                nextPixel = img[i+1, j+1]
            
            #If the intensity of the current pixel is greater than the previous or next pixel, assign the value in the non max matrix
            if((img[i, j] >= prevPixel) and (img(i,j) >= nextPixel)):
                nonMaxMatrix[i, j] = img[i][j]   
    
    # Return the matrix
    return nonMaxMatrix






def gradient_calculation():
    print("placeholder")

def double_threshold():
    print("placeholder")

def hysteresis():
    print("placeholder")

if __name__ == "__main__":
    main()
