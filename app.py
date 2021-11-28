import os
import cv2
import numpy as np
from scipy import ndimage
from customCanny import *
from imageai.Detection.Custom import CustomObjectDetection

def main():
    # Run the Custom Canny Algorithm
    filePath = "./TestImages/testImage2.jpg"
    # Get the file name to better print the output
    indexSlash = filePath.rfind('/')
    indexPeriod = filePath.rfind('.')
    remove = len(filePath) - indexPeriod
    fileName = filePath[indexSlash+1:-remove]
    # If the directory does not exist, make it
    if (not os.path.exists("./Output/" + fileName)):
        os.mkdir("./Output/" + fileName);
    # Get the edge detected image
    edge_img = runAlgorithm(filePath)
    # Set up the model to detect the mask
    detector = CustomObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath("./headsets/models/detection_model-ex-010--loss-0015.353.h5")
    detector.setJsonPath("./headsets/json/detection_config.json")
    detector.loadModel()
    # Concatenate the edge_ to the file path
    input_img = "./Output/" + fileName + "/edge_" + fileName + ".jpg";
    detections = detector.detectObjectsFromImage(input_image=input_img, output_image_path="./Output/" + fileName + "/" + "mask_" + fileName + ".jpg")
    for detection in detections:
        print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])

if __name__ == "__main__":
    main()
