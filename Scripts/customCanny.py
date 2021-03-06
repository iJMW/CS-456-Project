import cv2
import numpy as np
from scipy import ndimage

def main():
    # Read the image
    img = cv2.imread("./TestImages/testImage.jpg")
    # Resize the image
    img = cv2.resize(img, (500, 500))
    # Set the image to grayscale
    img = np.float32(cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY))
    img = img / img.max()
    cv2.imshow('image', img)
    cv2.waitKey(0)
    
    # Get the noised reduced image
    img = noise_reduction(img, 10, 1.5)
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
         
def runAlgorithm(filePath, folderName, fileName):
    # Read the image
    img = cv2.imread(filePath)
    img = cv2.resize(img, (500, 500))
    # Set the image to grayscale
    img = np.float32(cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY))
    img = img / img.max()
    
    # Get the noised reduced image
    img = noise_reduction(img, 10, 1.5)
    
    # Get gradient calculated image
    g, slope = gradient_calculation(img)
    
    # Non-Max Suppression
    img = non_max_suppression(g, slope)

    # double-threshold Suppression
    img = double_threshold(img, 0.05, 0.15)

    # hy Suppression
    img = hysteresis(img)

    # Write the file
    filepath = folderName + "/" + "input_" + fileName + ".jpg"
    cv2.imwrite(filepath, img)
    
    # Return the image
    return filepath
    
def noise_reduction(img, size, sigma):
    #set size
    size = size // 2
    #set kernel x and y
    x, y = np.mgrid[-size:size+1, -size:size+1]
    #normalize
    normal = 1 / (2.0 * np.pi * sigma**2)
    #create kernel
    kernel =  np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
    #apply kernel to image
    conv_img = ndimage.filters.convolve(img, kernel)
    return conv_img

def gradient_calculation(img):
    # Kernel in the x-directional
    Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
    # Kernel in the y directional
    Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)

    # Intensity changes in x
    Ix = ndimage.filters.convolve(img, Kx)
    # Intensity changes in the y direction
    Iy = ndimage.filters.convolve(img, Ky)

    #calculate gradiant
    GradMatrix = np.hypot(Ix, Iy)
    
    GradMatrix = GradMatrix / GradMatrix.max()
    #convert to float32
    GradMatrix = np.float32(GradMatrix)
    #calculate angles using arctan function
    Angles = np.arctan2(Iy, Ix)

    return (GradMatrix, Angles)

# Gets rid of extra edges
def non_max_suppression(img, angleDirection):
    #Gets the size of the image
    (row, col) = img.shape
    #Creates a matrix of zeros
    nonMaxMatrix = np.zeros((row, col), dtype=np.float32)
    # Get the angle
    angle = angleDirection * 180. / np.pi
    # Any values less than 0, add 180 to them
    angle[angle < 0] += 180

    #Iterates over all the pixels
    for i in range(1, row-1):
        for j in range(1, col-1):
            #Assigns the neighboring pixels adjacent to the current pixel
            prevPixel = img[i, j]
            nextPixel = img[i, j]

            #Checks the pixels on the left and right
            if((0 <= angleDirection[i, j] < np.pi/4) or (7*np.pi/4 <= angleDirection[i, j] < 2*np.pi)):
                prevPixel = img[i, j-1]
                nextPixel = img[i, j+1]
            #Checks the pixels on the top right and bottom left
            elif((np.pi/4 <= angleDirection[i, j] < np.pi/2) or (5*np.pi/4 <= angleDirection[i, j] < 3*np.pi/2)):
                prevPixel = img[i+1, j-1]
                nextPixel = img[i-1, j+1]
            #Checks the pixels on the top middle and bottom middle
            elif((np.pi/2 <= angleDirection[i, j] < 3*np.pi/4) or (3*np.pi/2 <= angleDirection[i, j] < 7*np.pi/4)):
                prevPixel = img[i-1, j-1]
                nextPixel = img[i+1, j+1]
            #Checks the pixels on the top left and bottom right
            #Default case
            else:
                prevPixel = img[i-1, j-1]
                nextPixel = img[i+1, j+1]
            
            #If the intensity of the current pixel is greater than the previous or next pixel, assign the value in the non max matrix
            if((img[i, j] >= prevPixel) and (img[i,j] >= nextPixel)):
                nonMaxMatrix[i, j] = img[i, j]
            else:
                nonMaxMatrix[i, j] = 0 
    
    # Return the matrix
    return nonMaxMatrix

def double_threshold(img, lowRatio, highRatio):
    # Get the pixel value that will be used to classify other pixels as strong
    highValue = highRatio * img.max()
    # Get the pixel value that will be used to classify other pixels as weak
    lowValue = lowRatio * highValue

    # Get the row and column size of the image
    m, n = img.shape
    
    # Create a resulting 2D array
    res = np.zeros((m, n), dtype=np.float32)

    # Grey color used to make weak pixels
    grey = np.uint8(25)
    # White color used to mark strong pixels
    white = np.uint8(255)

    # Get the locations of all the pixels with values greater than the high value
    # These are known as strong pixels
    strongX, strongY = np.where(img >= highValue)
    # Get the locations of all the pixels with values less than the high value 
    # but greater than the low value
    # These are known as weak pixels
    weakX, weakY = np.where((img < highValue) & (img >= lowValue))

    # Set all the strong pixels to white
    res[strongX, strongY] = white
    # Set all the weak pixels to grey
    res[weakX, weakY] = grey

    # Return the resulting image
    return res

def hysteresis(img):
    # Get the row and columns of the image
    m, n = img.shape

    # Grey color used to find weak pixels
    grey = np.float32(25)
    # White color used to mark strong pixels
    white = np.float32(255)

    # Top to bottom
    # Iterate through the rows
    for i in range(1, m-1):
        # Iterate through the columns
        for j in range(1, n-1):
            # If a weak pixel is detected
            # A weak pixel has a grey color
            if (img[i, j] == grey):
                try:
                    # Check if any of the 8-neighbors are a strong pixel
                    if (img[i-1, j-1] == white or img[i-1, j] == white or img[i-1, j+1] == white
                        or img[i, j-1] == white or img[i, j+1] == white
                        or img[i+1, j-1] == white or img[i+1, j] == white or img[i+1, j+1] == white):
                        # If one of the 8-neighbors is a strong pixel, set this pixel to a strong pixel
                        img[i, j] = white
                    else: 
                        # Else, set the pixel to black
                        img[i, j] = 0
                # Catch the index out of bounds error and continue
                except IndexError:
                    pass

    return img

if __name__ == "__main__":
    main()
