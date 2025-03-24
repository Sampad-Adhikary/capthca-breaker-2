import tensorflow as tf
import numpy as np
import cv2

import matplotlib.image as mpimg

def convert_to_black_and_white(image_path, output_path):
    # Read the image using Matplotlib
    image = mpimg.imread(image_path)

    # convert to grayscale
    


# Example usage
image_path = "input/captcha-version-2-images/samples/ndxnb.png"  # Replace with your image path
output_path = "output.jpg"
convert_to_black_and_white(image_path, output_path)