# Early Detection of Shockable and Non-Shockable Arrhythmia

This Django web application uses a hybrid pooling model to detect arrhythmia types from ECG images.

## Features

- Upload ECG images for arrhythmia classification
- Predicts one of 5 classes: L (Left Bundle Branch Block), N (Normal), P (Paced), R (Right Bundle Branch Block), V (Ventricular Premature Beat)
- Clean, responsive UI built with Tailwind CSS

## Setup Instructions

1. Ensure you have Python installed (3.8+ recommended).

2. Install dependencies:
   ```
   pip install django tensorflow numpy pillow
   ```

3. Place your trained model file `Hybrid_1.h5` in the `detector/` directory.

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

6. Open your browser and go to `http://127.0.0.1:8000/`

## Project Structure

- `arrhythmia_detection/`: Main Django project directory
- `detector/`: Django app containing the arrhythmia detection logic
  - `model_utils.py`: Model loading and prediction functions
  - `views.py`: Handles upload and prediction
  - `templates/detector/`: HTML templates
- `media/`: Directory for uploaded images (created automatically)

## Model Requirements

The application expects a Keras model saved in HDF5 format with a custom `MaxMinPooling2D` layer. The model should be trained on 224x224 RGB images and output predictions for 5 classes.

## Usage

1. On the home page, click "Choose File" to select an ECG image.
2. Click "Predict Arrhythmia" to get the classification result.
3. The result page shows the predicted class, description, and confidence score.

## Notes

- The model is loaded lazily on first prediction to avoid startup delays.
- Uploaded images are temporarily stored and deleted after processing.
- For production deployment, consider using a proper file storage service and adding authentication.