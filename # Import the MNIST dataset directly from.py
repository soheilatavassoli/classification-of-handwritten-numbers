# Import the MNIST dataset directly from Keras
from tensorflow.keras.datasets import mnist

# Load training and testing data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize pixel values to a range between 0 and 1
# This helps the neural network learn more efficiently
x_train = x_train / 255.0
x_test = x_test / 255.0

# Print a confirmation message to ensure successful dataset import
print("MNIST dataset has been successfully loaded and preprocessed!")


# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense

# Commonly used modules
import numpy as np
import os
import sys

# Images, plots, display, and visualization
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import cv2
import IPython
from six.moves import urllib

print(tf.__version__)

# Set common constants
this_repo_url = 'https://github.com/arunkumarramanan/mit-deep-learning/raw/master/'
this_tutorial_url = this_repo_url + 'tutorial_deep_learning_basics'


