# Footballer Classifier

## Introduction

Welcome to the Footballer Classifier project! This project focuses on classifying images of football celebrities using machine learning. The dataset comprises various images obtained from the internet, covering 7 classes with a total of 673 images. The data preprocessing involves face and eye detection using Haar Cascade Classifiers, generating cropped images, and applying wavelet transformation for feature extraction.

## Dataset

- **Size:** 673 images
- **Classes:** 7 (football celebrities)
- **Preprocessing:** Haar Cascade Classifiers, Cropping, Wavelet Transformation

## Data Preprocessing

### Haar Cascade Classifiers

The Haar Cascade Classifiers for face and eye detection are essential for localizing facial features in images.

### Face Detection

The `detectMultiScale` function identifies faces in grayscale images, and the resulting rectangles are stored.

### Cropping

Images are cropped around detected faces, focusing on the region of interest.

### Wavelet Transformation

The `w2d` function applies a 2D wavelet transform to images, capturing essential features.

## Model Training

A machine learning pipeline is employed, featuring a grid search over Support Vector Machine (SVM), Random Forest, and Logistic Regression classifiers. The best-performing model, Logistic Regression, achieves an accuracy of approximately 81.32% on the test set.

## Deployment

The model is deployed using a Flask web application. Users can upload images, and the application provides real-time predictions. The model is loaded during startup, ensuring quick and efficient classification.

## How to Use

1. Clone the repository.
2. Install the required dependencies.
3. Run the Flask application (`app.py`).
4. Access the application through a web browser.
5. Upload an image for classification.

Feel free to explore the code, experiment with the models, and contribute to the project!

## Acknowledgments

Special thanks to the creators of Haar Cascade Classifiers, scikit-learn, Flask, and other libraries that contribute to the success of this project.

Enjoy recognizing your favorite football celebrities!
