import cv2
import numpy as np
from scipy import ndimage
from customCanny import *
from imageai.Detection.Custom import CustomObjectDetection

def main():
    # Run the Custom Canny Algorithm
    filePath = "testImage.jpg"
    edge_img = runAlgorithm(filePath)
    detector = CustomObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath("./headsets/models/detection_model-ex-010--loss-0015.353.h5")
    detector.setJsonPath("./headsets/json/detection_config.json")
    detector.loadModel()
    #Concatenate the edge_ to the file path
    input_img = "edge_" + filePath
    detections = detector.detectObjectsFromImage(input_image=input_img, output_image_path="mask-detected.jpg")
    for detection in detections:
        print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])

if __name__ == "__main__":
    main()
