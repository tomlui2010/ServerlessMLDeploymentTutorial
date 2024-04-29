import json
import base64

from io import BytesIO
from PIL import Image

import keras
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

import numpy as np

# Import the saved pre-trained model and build  
# model = tf.keras.Sequential([hub.KerasLayer("/opt/ml/model/")])
# model.build([None, 224, 224, 3])
# imagenet_labels= np.array(open('/opt/ml/model/ImageNetLabels.txt').read().splitlines())

# Using Keras library to import ResNet50 model
model = ResNet50(weights='imagenet')

# Define the image size
img_height, img_width = 224, 224

# Preprocess image to the right mode, size that is feasible with the pre-trained model
def preprocess_image(image):

    # Convert image to RGB mode
    image = image.convert('RGB')
    # Change the size of the image to the size with which model has been trained
    image = image.resize((img_height, img_width))
    # Use img_to_array() function to adds channels
    image_array = keras.utils.img_to_array(image)
    # Use expand_dims() to add the number of images
    image_array = np.expand_dims(image_array, axis=0)
    # Use preprocess_input to subtract the mean RGB channels of the imagenet dataset
    image_array = preprocess_input(image_array)
    return image_array

def lambda_handler(event, context):
    # Print the event object
    # print("Received event:")
    # print(json.dumps(event, indent=4))
    # Image is received as a base64 encoded through the event object
    image_data = base64.b64decode(event['body'])
    # Decode the image data and convert it to BytesIO object to open the image
    image = Image.open(BytesIO(image_data))
    # Preprocess image to the right parameters required for the pre-trained model
    image = preprocess_image(image)
    # models prediction
    prediction = model.predict(image)
    # Use decode_predictions to parse the model's prediction to get top3 results
    message = decode_predictions(prediction, top=3)[0]
    print('Predicted:', message)
    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                "predicted_label_top3": str(message)
            }
        )
    }
