from imageai.Detection.Custom import CustomObjectDetection

def detect(folderName, fileName, modelDecision):
    # Set up the model to detect the mask
    detector = CustomObjectDetection()
    detector.setModelTypeAsYOLOv3()
    # Set the appropriate model based on user sleected
    if (modelDecision == 0):
        # Set the model to the edge detected images model
        detector.setModelPath("./headsets/models/detection_model-ex-010--loss-0015.353.h5")
        detector.setJsonPath("./headsets/json/detection_config.json")
    else:
        # Set the model to the original images model
        detector.setModelPath("./headsets3/models/detection_model-ex-009--loss-0014.014.h5")
        detector.setJsonPath("./headsets3/json/detection_config.json")
    # Load the model
    detector.loadModel() 
    # Set the input image path
    input_img = folderName + "/input_" + fileName + ".jpg"
    print("Input Path: " + input_img)
    # Set the output image path
    output_img_path = folderName + "/" + "output_" + fileName + ".jpg"
    # Detect the objects in the images and output the image
    detections = detector.detectObjectsFromImage(input_image=input_img, output_image_path=output_img_path)
    # For each detection in the detected image, output the coordinates of the detected object
    for detection in detections:
        print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
    # Return the output image path
    return output_img_path
