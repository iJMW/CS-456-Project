import cv2
import numpy as np

def main():
    print("placeholder")

def noise_reduction():
    print("placeholder")

def non_max_suppression():
    print("Placeholder")

def gradient_calculation():
    print("placeholder")

def double_threshold(img, lowRatio, highRatio):
    # Get the pixel value that will be used to classify other pixels as strong
    highValue = highRatio * img.max()
    # Get the pixel value that will be used to classify other pixels as weak
    lowValue = lowRatio * highValue

    # Get the row and column size of the image
    m, n = img.shape
    
    # Create a resulting 2D array
    res = np.zeros((m, n), dtype=np.int32)

    # Grey color used to make weak pixels
    grey = np.int32(25)
    # White color used to mark strong pixels
    white = np.int32(255)

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
    grey = np.int32(25)
    # White color used to mark strong pixels
    white = np.int32(255)

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

if __name__ == "__main__":
    main()
