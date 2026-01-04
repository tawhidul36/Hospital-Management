# import tensorflow as tf
# import numpy as np
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import os

# # Define the custom layer
# class MaxMinPooling2D(tf.keras.layers.Layer):
#     def __init__(self, pool_size=(2, 2), **kwargs):
#         super(MaxMinPooling2D, self).__init__(**kwargs)
#         self.pool_size = pool_size

#     def build(self, input_shape):
#         super(MaxMinPooling2D, self).build(input_shape)

#     def call(self, inputs):
#         max_pooling = tf.keras.layers.MaxPooling2D(pool_size=self.pool_size)(inputs)
#         min_pooling = -tf.keras.layers.MaxPooling2D(pool_size=self.pool_size)(-inputs)
#         return tf.concat([max_pooling, min_pooling], axis=-1)

#     def compute_output_shape(self, input_shape):
#         return (input_shape[0], input_shape[1] // 2, input_shape[2] // 2, input_shape[3] * 2)

# # Load model lazily
# MODEL_PATH = os.path.join(os.path.dirname(__file__), 'Hybrid_1.h5')
# model = None

# def get_model():
#     global model
#     if model is None:
#         model = load_model(MODEL_PATH, custom_objects={'MaxMinPooling2D': MaxMinPooling2D})
#     return model

# # Input shape
# img_height, img_width = 224, 224

# # Class labels
# class_names = ['L', 'N', 'P', 'R', 'V']

# # Preprocessing function
# def preprocess_image(img_path):
#     img = image.load_img(img_path, target_size=(img_height, img_width))
#     img_array = image.img_to_array(img) / 255.0  # scale to [0,1]
#     return np.expand_dims(img_array, axis=0)

# # Prediction function
# def predict_arrhythmia(img_path):
#     img_array = preprocess_image(img_path)
#     model = get_model()
#     predictions = model.predict(img_array, verbose=0)
#     predicted_class_index = np.argmax(predictions[0])
#     predicted_class = class_names[predicted_class_index]
#     confidence = predictions[0][predicted_class_index] * 100  # as percentage
#     return predicted_class, confidence