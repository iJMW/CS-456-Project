# Import ImageAI detection model training class
from imageai.Detection.Custom import DetectionModelTrainer
# Define model trainer
trainer = DetectionModelTrainer()
# Set the network type
trainer.setModelTypeAsYOLOv3()
# Set the path to the image dataset we want to train the network on
trainer.setDataDirectory(data_directory="headsets")
# Configure the detection model trainer
trainer.setTrainConfig(object_names_array=["mask"], batch_size=4, num_experiments=10, train_from_pretrained_model="pretrained-yolov3.h5")
# Test 1:
# trainer.setTrainConfig(object_names_array=["mask"], batch_size=4, num_experiments=10, train_from_pretrained_model="pretrained-yolov3.h5")
# 
# Train the model
trainer.trainModel()