from imageai.Detection.Custom import CustomObjectDetection

def detect(fileName):
    # Set up the model to detect the mask
    detector = CustomObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath("./headsets/models/detection_model-ex-010--loss-0015.353.h5")
    detector.setJsonPath("./headsets/json/detection_config.json")
    detector.loadModel()
    # Concatenate the edge_ to the file path
    input_img = "./Output/" + fileName + "/edge_" + fileName + ".jpg";
    print("Input Image Path Detector: " + input_img)
    output_img_path = "./Output/" + fileName + "/" + "mask_" + fileName + ".jpg"
    print("Output Image Path Detector: " + output_img_path)
    detections = detector.detectObjectsFromImage(input_image=input_img, output_image_path="./Output/" + fileName + "/" + "mask_" + fileName + ".jpg")
    for detection in detections:
        print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
    return output_img_path
