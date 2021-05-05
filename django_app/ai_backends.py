from django.conf import settings

import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input

from io import BytesIO
from PIL import Image
import requests


def loadImage(url):
    response = requests.get(url)
    img_bytes = BytesIO(response.content)
    img = Image.open(img_bytes)
    img = img.convert('RGB')
    img = img.resize((224, 224), Image.NEAREST)

    return img

def ai_test(url):
    trained_model = load_model('ai_model\chest_xray.h5', compile=False)
    img = loadImage(url)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    img_data = preprocess_input(x)
    classes = trained_model.predict(img_data)
    result = int(classes[0][0])
    return result