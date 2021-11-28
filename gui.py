# Import custom canny algorithm implementation
from numpy.core.fromnumeric import size
from customCanny import *
from detector import *

# Import libraries
import tkinter
from tkinter import *
from tkinter import filedialog
import PIL.Image
import PIL.ImageTk
import os

# Main file to run for GUI
class Gui:
    
    def __init__(self, window, window_title, video_source=0):
        # Determines if an image has been edge detected
        self.edge_detected = False;
        # Sets the window to be opened of the object
        self.window = window
        # Sets the title of the window of the object
        self.window.title(window_title)
        # Sets the size of the window
        self.window.geometry("1500x1000")
        self.window.configure(bg = "white")

        # Divide the window into two halves
        self.left_frame = Frame(self.window, bg= "white")
        self.left_frame.pack(side = TOP)
        self.right_frame =  Frame(self.window, bg= "white")
        self.right_frame.pack(side = BOTTOM)

        # Creates title
        self.title_label = tkinter.Label(self.left_frame, text = "Image", font=("Times New Roman", 20))
        self.title_label.grid(row=0)
        
        # Add a initilize image
        self.file_name = "testImage"
        self.file_path = "./TestImages/testImage.jpg"
        self.folder_name = "TestImages"
        original_img = PIL.Image.open(self.file_path)
        original_img = original_img.resize((750, 500))
        self.img = PIL.ImageTk.PhotoImage(original_img)
        self.image_label = tkinter.Label(self.left_frame, image = self.img)
        self.image_label.grid(row = 1)     

        # Creates a open file button
        self.open_image_button = tkinter.Button(self.right_frame, text = "Open Image", command = lambda: self.getInputImage())
        self.open_image_button.grid(row=2, column = 1, padx = 20, pady = 20)

        # Creates a run canny algorithm
        self.trainer_button = tkinter.Button(self.right_frame, text = "Run Canny Algorithm", command = lambda: self.runCannyAlgorithm())
        self.trainer_button.grid(row=2, column = 2, padx = 20, pady = 20)
        
        # Creates a mask detect button
        self.recognize_button = tkinter.Button(self.right_frame, text = "Detect Mask(s)", command = lambda: self.detect())
        self.recognize_button.grid(row=2, column = 3, padx = 20, pady = 20)
        
        # Run the GUI
        self.window.mainloop()

    # Used to open a file dialog to get the image
    def getInputImage(self):
        # Get the path to the image
        self.file_path = filedialog.askopenfilename()
        # Update the file name
        self.file_name = self.getFileName()
        # Update the GUI
        self.updateImage()
        # Set the image has not been edge detected
        self.edge_detected = False
        # Update the label
        self.title_label.config(text="Image")
    
    # Used to run the canny algorithm
    def runCannyAlgorithm(self):
        self.folder_name = "./Output/" + self.file_name;
        # Make a directory with the file name if it doesn't exist for the output images
        if (not os.path.exists(self.folder_name)):
            os.mkdir(self.folder_name)
        # Run the algorithm
        self.file_path = runAlgorithm(self.file_path)
        # Update the GUI
        self.updateImage()
        # Set that the image has been edge detected
        self.edge_detected = True
        # Update the label
        self.title_label.config(text="Edge Detected Image")

    # Used to detect a mask in an image
    def detect(self):
        # Only let the user detect masks in edge detected images
        if(self.edge_detected):
            # Run the detector
            self.file_path = detect(self.file_name)
            # Update the GUI
            self.updateImage()
            # Update the label
            self.title_label.config(text="Mask Detected Image")

    # Used to update the image in the GUI
    def updateImage(self):
        # Update the image in the GUI
        original_img = PIL.Image.open(self.file_path)
        original_img = original_img.resize((750, 500))
        self.img = PIL.ImageTk.PhotoImage(original_img)
        self.image_label.configure(image=self.img)
        self.image_label.image = self.img

    # Used to get the file name
    def getFileName(self):
        # Get the file name to better print the output
        indexSlash = self.file_path.rfind('/')
        indexPeriod = self.file_path.rfind('.')
        remove = len(self.file_path) - indexPeriod
        fileName = self.file_path[indexSlash+1:-remove]
        return fileName

Gui(tkinter.Tk(), "CS 456 Project")