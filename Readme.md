## MNIST Digit Classification with CNN

This project implements a Convolutional Neural Network (CNN) to classify handwritten digits from the famous **MNIST** dataset. Additionally, the trained model is tested on a video containing high-resolution images.

## Project Team Members
- Fatemeh Saeidi  
- Soheila Tavassoli  
- Elisa Chateri

## Project Structure

- **Dataset:** MNIST from Keras  
- **Preprocessing:** Image normalization, reshaping, and grayscale conversion  
- **Model:** Using `Conv2D`, `MaxPooling2D`, `Dropout`, `Flatten`, and `Dense` layers  
- **Training:** The model is trained for 5 epochs and achieves nearly **99%** accuracy on the test data  
- **Highlight:** Testing the model on a high-resolution image video (MNIST dreams)

## Technologies and Libraries

- Python 3  
- TensorFlow / Keras  
- OpenCV  
- NumPy  
- Matplotlib

## Results Preview

![MNIST dream predictions](https://i.imgur.com/eMF9FOG.gif)

## Running the Project

To run the project, follow these steps:

1. Install the required libraries:
```bash
pip install -r requirements.txt

