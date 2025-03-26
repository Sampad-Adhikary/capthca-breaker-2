import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

mypath = '1/'
output = 'input/captcha-version-2-images/samples/'
images = [f'{mypath}{f}' for f in listdir(mypath) if isfile(join(mypath, f))]

def resize_and_pad(image, target_width=200, target_height=50):
    # Get current dimensions
    h, w = image.shape[:2]

    # Resize the width to 200 while keeping height the same
    resized = cv2.resize(image, (target_width, target_height), interpolation=cv2.INTER_LINEAR)

    return resized

print(images)

for img in images:
    img_path = img
    print(img.split("/")[-1])
    if len(img.split("/")[-1]) != 9:
        continue
    # take the file name and add it to the output path
    output_path = f'{output}{img.split("/")[-1]}'
    # Load an image
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)  # Read as grayscale
    resized_image = resize_and_pad(image)
    print(output_path)
    # Save or display the resized image
    cv2.imwrite(output_path, resized_image)
