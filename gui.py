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
    
    # Initialize the window with the appropriate widgets
    def __init__(self, window, window_title, video_source=0):
        # Determines if the user has selected an image
        self.selected_image = False
        # Determines if an image has been edge detected
        self.edge_detected = False
        
        # Sets the window to be opened of the object
        self.window = window
        # Sets the title of the window of the object
        self.window.title(window_title)
        # Sets the size of the window
        self.window.geometry("1500x1000")
        self.window.configure(bg = "white")

        # Divide the window into two halves, a top and bottom
        self.top_frame = Frame(self.window)
        self.top_frame.pack(side = TOP)
        self.bottom_frame =  Frame(self.window, bg= "white")
        self.bottom_frame.pack(side = BOTTOM)

        # Creates title
        self.title_label = tkinter.Label(self.top_frame, text = "Image", font=("Times New Roman", 20))
        self.title_label.grid(row=0)
        
        # Add a initilize image
        self.file_name = "defaultImage"
        self.file_path = "./defaultImage.jpg"
        self.folder_name = ""
        original_img = PIL.Image.open(self.file_path)
        original_img = original_img.resize((750, 500))
        self.img = PIL.ImageTk.PhotoImage(original_img)
        self.image_label = tkinter.Label(self.top_frame, image = self.img)
        self.image_label.grid(row = 1, pady = 20)     

        # Create a drop down box
        self.clicked = StringVar()
        self.clicked.set("Edge Detected Images Model")
        self.drop_down = tkinter.OptionMenu(self.bottom_frame, self.clicked, *["Edge Detected Images Model", "Original Images Model"])
        self.drop_down.grid(row=1, column = 0, padx = 20, pady = 20)

        # Creates a open file button
        self.open_image_button = tkinter.Button(self.bottom_frame, text = "Open Image", command = lambda: self.getInputImage())
        self.open_image_button.grid(row=1, column = 1, padx = 20, pady = 20)

        # Creates a run canny algorithm
        self.trainer_button = tkinter.Button(self.bottom_frame, text = "Run Canny Algorithm", command = lambda: self.runCannyAlgorithm())
        self.trainer_button.grid(row=1, column = 2, padx = 20, pady = 20)
        
        # Creates a mask detect button
        self.recognize_button = tkinter.Button(self.bottom_frame, text = "Detect Mask(s)", command = lambda: self.detect())
        self.recognize_button.grid(row=1, column = 3, padx = 20, pady = 20)
        
        # Run the GUI
        self.window.mainloop()

    # Used to open a file dialog to get the image
    def getInputImage(self):
        # Get the path to the image from the open file dialog
        file_path = filedialog.askopenfilename()
        # Check that the user did not hit "Cancel"
        if (file_path):
            # Update the file path to the image
            self.file_path = file_path
            # Update the file name
            self.file_name = self.getFileName()
            # Update the GUI
            self.updateImage()
            # Set the image has not been edge detected
            self.edge_detected = False
            # Update the label
            self.title_label.config(text="Image")
            # Set that the user has selected an image
            self.selected_image = True
    
    # Used to run the canny algorithm
    def runCannyAlgorithm(self):
        # If the user has selected an image
        if (self.selected_image):
            # Set the folder name to the output folder
            self.folder_name = "./Output/" + self.clicked.get().replace(" ", "") + "_" + self.file_name
            # Make a directory with the file name if it doesn't exist for the output images
            if (not os.path.exists(self.folder_name)):
                os.mkdir(self.folder_name)
            # Run the algorithm
            self.file_path = runAlgorithm(self.file_path, self.folder_name, self.file_name)
            # Update the GUI
            self.updateImage()
            # Set that the image has been edge detected
            self.edge_detected = True
            # Update the label
            self.title_label.config(text="Edge Detected Image")
        # Display an error message that the user has not selected an image
        else:
            print(self.selected_image)
            print(self.clicked.get())
            errorMessage = "Please select an image"
            tkinter.messagebox.showerror("Error", errorMessage)

    # Used to detect a mask in an image
    def detect(self):
        # Update the expected folder name
        self.folder_name = "./Output/" +  self.clicked.get().replace(" ", "") + "_" + self.file_name
        # Check that the expected folder exists
        if (not os.path.exists(self.folder_name)):
            # If the directory does not exist, create it
            os.mkdir(self.folder_name)
        # Write the image to the directory
        cv2.imwrite(self.folder_name + "/input_" + self.file_name + ".jpg", cv2.imread(self.file_path))
        #  Check that the user selected an image
        if (self.selected_image):
            # Determine which model the user selected
            if(self.clicked.get() == "Edge Detected Images Model"):
                # Run the detector with the model created from the edge detected images
                self.file_path = detect(self.folder_name, self.file_name, 0)
            elif (self.clicked.get() == "Original Images Model"):
                # Run the detector with the model created from the original images
                self.file_path = detect(self.folder_name, self.file_name, 1)
            # Update the GUI
            self.updateImage()
            # Update the label
            self.title_label.config(text="Mask Detected Image")
        # Display an error telling the user to select an image
        else:
            errorMessage = "Please select an image"
            tkinter.messagebox.showerror("Error", errorMessage)

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