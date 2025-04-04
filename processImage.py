import cv2
import numpy as np
import os

mypath = '2/'
output_path = '2/'
os.makedirs(output_path, exist_ok=True)

image_paths = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
# image_paths = ['/home/invincibleocean/Work/cnn-captcha-solver/captcha_images/3bm63.png']
for image_path in image_paths:
    print(f'Processing {image_path}')
    
    # Read image in unchanged mode
    captcha_img_rgba = cv2.imread(os.path.join(mypath, image_path), cv2.IMREAD_UNCHANGED)

    # Extract alpha channel (if available) or convert to grayscale
    if captcha_img_rgba.shape[2] == 4:
        print('Alpha channel avaliable')
        alpha_channel = captcha_img_rgba[:, :, 3]
        text_mask = cv2.bitwise_not(alpha_channel)
    else:
        text_mask = cv2.cvtColor(captcha_img_rgba, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to binarize the image
    _, text_thresh = cv2.threshold(text_mask, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Detect horizontal lines
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1))  # Adjust kernel size based on line thickness
    horizontal_lines = cv2.morphologyEx(text_thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    # Subtract detected lines from the original thresholded image
    text_cleaned = cv2.bitwise_or(text_thresh, horizontal_lines)


    kernel_thin = np.ones((1, 1), np.uint8)  # Increase height of erosion
    text_thinned = cv2.erode(text_cleaned, kernel_thin, iterations=30)  # More aggressive erosion

    kernel_thin = np.ones((1, 1), np.uint8)  # Increase height of dilation
    text_thinned = cv2.dilate(text_thinned, kernel_thin, iterations=30)

    # Save the processed image
    cv2.imwrite(os.path.join(output_path, image_path), text_thinned)

print("Processing complete. Cleaned CAPTCHA images are saved in", output_path)

