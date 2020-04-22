import cv2
import numpy as np
from django.conf import settings
from keras.models import model_from_json


class Model():
    def __init__(self):
        path = '{}/model.json'.format(settings.MODEL_DIR)
        with open(path, 'r') as f:
            self.model = model_from_json(f.read())
            self.model.load_weights(path.replace('json', 'h5'))
        self.threshold = 0.00003051757

    def predict(path):
        pred = self.model.predict(self.load_image(path))[0]
        pred[pred > self.threshold] = 0
        pred = pred / self.threshold
        return pred

    def load_image(path):
        return cv2.resize(cv2.imread(path), (1024, 1024)).reshape(1, 1024, 1024, 3).astype('float32') / 255
