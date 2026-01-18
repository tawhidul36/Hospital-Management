import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class MaxMinPooling2D(tf.keras.layers.Layer):
    def __init__(self, pool_size=(2, 2), **kwargs):
        super().__init__(**kwargs)
        self.pool_size = pool_size

    def call(self, inputs):
        max_pool = tf.keras.layers.MaxPooling2D(self.pool_size)(inputs)
        min_pool = -tf.keras.layers.MaxPooling2D(self.pool_size)(-inputs)
        return tf.concat([max_pool, min_pool], axis=-1)

MODEL_PATH = "Hybrid_1.h5"
model = None

class_names = ['L', 'N', 'P', 'R', 'V']
img_height, img_width = 224, 224

def get_model():
    global model
    if model is None:
        model = load_model(
            MODEL_PATH,
            custom_objects={'MaxMinPooling2D': MaxMinPooling2D}
        )
    return model

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(img_height, img_width))
    arr = image.img_to_array(img) / 255.0
    return np.expand_dims(arr, axis=0)

def predict_arrhythmia(img_path):
    model = get_model()
    img = preprocess_image(img_path)
    preds = model.predict(img, verbose=0)

    idx = np.argmax(preds[0])
    return {
        "class": class_names[idx],
        "confidence": float(preds[0][idx] * 100)
    }
