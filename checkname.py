import cv2
import numpy as np
import os

mypath = 'input/captcha-version-2-images/samples/'
output_path = 'input/captcha-version-2-images/samples/'
os.makedirs(output_path, exist_ok=True)

image_paths = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
# image_paths = ['/home/invincibleocean/Work/cnn-captcha-solver/captcha_images/3bm63.png']
for image_path in image_paths:
    name = image_path.split('.')[0]
    # print(name)
    if len(name) != 5:
        print(image_path)